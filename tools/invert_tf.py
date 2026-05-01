#!/usr/bin/env python3
import json
import math
import argparse

def invert_transform(input_file, output_file):
    # Load JSON file
    with open(input_file, 'r') as f:
        data = json.load(f)

    # 1. Swap frame_id and child_frame_id
    original_frame_id = data['header']['frame_id']
    original_child_frame_id = data['child_frame_id']
    
    data['header']['frame_id'] = original_child_frame_id
    data['child_frame_id'] = original_frame_id

    # 2. Get current translation (t) and rotation (q)
    tx = data['transform']['translation']['x']
    ty = data['transform']['translation']['y']
    tz = data['transform']['translation']['z']
    
    qx = data['transform']['rotation']['x']
    qy = data['transform']['rotation']['y']
    qz = data['transform']['rotation']['z']
    qw = data['transform']['rotation']['w']

    # --- Math calculations for inverse transform start here ---

    # A. Inverse rotation (Conjugate of quaternion: negate x, y, z)
    inv_qx, inv_qy, inv_qz, inv_qw = -qx, -qy, -qz, qw

    # B. Inverse translation: t_inv = -(R_inv * t)
    # First, calculate 3x3 rotation matrix (R_inv) from the inverse quaternion (inv_q)
    R00 = 1.0 - 2.0 * (inv_qy**2 + inv_qz**2)
    R01 = 2.0 * (inv_qx * inv_qy - inv_qz * inv_qw)
    R02 = 2.0 * (inv_qx * inv_qz + inv_qy * inv_qw)

    R10 = 2.0 * (inv_qx * inv_qy + inv_qz * inv_qw)
    R11 = 1.0 - 2.0 * (inv_qx**2 + inv_qz**2)
    R12 = 2.0 * (inv_qy * inv_qz - inv_qx * inv_qw)

    R20 = 2.0 * (inv_qx * inv_qz - inv_qy * inv_qw)
    R21 = 2.0 * (inv_qy * inv_qz + inv_qx * inv_qw)
    R22 = 1.0 - 2.0 * (inv_qx**2 + inv_qy**2)

    # Multiply matrix (R_inv) by vector (t) and negate
    inv_tx = -(R00 * tx + R01 * ty + R02 * tz)
    inv_ty = -(R10 * tx + R11 * ty + R12 * tz)
    inv_tz = -(R20 * tx + R21 * ty + R22 * tz)

    # C. Inverse Euler angles (Roll, Pitch, Yaw)
    # Standard formula to calculate Roll, Pitch, Yaw from the inverse quaternion (inv_q)
    sinr_cosp = 2.0 * (inv_qw * inv_qx + inv_qy * inv_qz)
    cosr_cosp = 1.0 - 2.0 * (inv_qx**2 + inv_qy**2)
    inv_roll = math.atan2(sinr_cosp, cosr_cosp)

    sinp = 2.0 * (inv_qw * inv_qy - inv_qz * inv_qx)
    if abs(sinp) >= 1:
        inv_pitch = math.copysign(math.pi / 2, sinp) # Protection if it exceeds 1.0 due to floating point error
    else:
        inv_pitch = math.asin(sinp)

    siny_cosp = 2.0 * (inv_qw * inv_qz + inv_qx * inv_qy)
    cosy_cosp = 1.0 - 2.0 * (inv_qy**2 + inv_qz**2)
    inv_yaw = math.atan2(siny_cosp, cosy_cosp)

    # --- Calculations end here ---

    # 3. Update JSON data
    data['transform']['translation']['x'] = inv_tx
    data['transform']['translation']['y'] = inv_ty
    data['transform']['translation']['z'] = inv_tz

    data['transform']['rotation']['x'] = inv_qx
    data['transform']['rotation']['y'] = inv_qy
    data['transform']['rotation']['z'] = inv_qz
    data['transform']['rotation']['w'] = inv_qw

    if 'roll' in data:
        data['roll'] = inv_roll
    if 'pitch' in data:
        data['pitch'] = inv_pitch
    if 'yaw' in data:
        data['yaw'] = inv_yaw

    # 4. Save as a new JSON file
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)
        
    print(f"=== Success ===")
    print(f"Original transform: {original_frame_id} -> {original_child_frame_id}")
    print(f"Inverse transform : {original_child_frame_id} -> {original_frame_id}")
    print(f"Result saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculates the inverse transform of a TF JSON file (uses only standard libraries).")
    parser.add_argument("input_file", help="Path to the input JSON file")
    parser.add_argument("output_file", help="Path to the output JSON file")
    args = parser.parse_args()

    invert_transform(args.input_file, args.output_file)