#!/bin/bash
export PATH=/usr/local/cuda/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH

perception_type=$1
if [ -z "$perception_type" ]; then
    echo "Usage: $0 <perception_type>"
    exit 1
fi

if [ "$perception_type" != "addon" ]; then
    echo "Applying BSP36.4 upgrade patches..."
    # TODO: This is a patch for BSP36.4 upgrade
    sed -i '/strategy::convex_hull::graham_andrew.*strategy;/d; /convex_hull(ring, convex_ring, strategy);/c\  boost::geometry::convex_hull(ring, convex_ring);' src/autoware.universe/common/autoware_universe_utils/src/geometry/random_concave_polygon.cpp
    sed -i 's|#include <boost/geometry/strategies/agnostic/hull_graham_andrew.hpp>|#include <boost/geometry/algorithms/detail/convex_hull/graham_andrew.hpp>|' src/autoware.universe/common/autoware_universe_utils/src/geometry/random_concave_polygon.cpp
    sed -i '/strategy::convex_hull::graham_andrew.*strategy;/d; /convex_hull(.*strategy);/c\  boost::geometry::convex_hull(ring, convex_ring);' src/autoware_utils/autoware_utils/src/geometry/random_concave_polygon.cpp
    sed -i 's|#include <boost/geometry/strategies/agnostic/hull_graham_andrew.hpp>|#include <boost/geometry/algorithms/detail/convex_hull/graham_andrew.hpp>|' src/autoware_utils/autoware_utils/src/geometry/random_concave_polygon.cpp
fi

if [ "$perception_type" = "addon" ]; then
    echo "Running rosdep update and install for addon..."
    rosdep update
    rosdep install --from-paths src --ignore-src -r -y
fi

colcon build \
    --symlink-install \
    --packages-up-to edge_auto_jetson_launch \
    --cmake-args -DCMAKE_BUILD_TYPE=Release \
    -DPython3_EXECUTABLE="$(which python3)" \
    -DCMAKE_CUDA_STANDARD=14 \
    -DCMAKE_POLICY_VERSION_MINIMUM=3.5

