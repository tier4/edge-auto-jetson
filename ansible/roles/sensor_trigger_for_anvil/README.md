# Sensor trigger for Anvil

この Role は TIER IV C2 カメラ向けのsensor triggerの設定をCTI Anvilに行う

## Role in system design

<!-- markdown-link-check-disable -->

CTI Anvil向けのTIER IV C2 カメラのsensor triggerの設定を行う.

<!-- markdown-link-check-enable -->

## Dependency

## Usage

### Variables

<!-- markdown-link-check-disable -->

<!-- markdown-link-check-enable -->

### Preparation

playbook への追加例

```yaml
vars:
  - { role: sensor_trigger_for_anvil, tags: [sensor_trigger_for_anvil] }
```

## Related links

<https://tier4.atlassian.net/wiki/spaces/NGSS1st/pages/3052504514/ConnectTech+Anvil+TIER+IV+camera+drivers+installation+For+X2+Gen2>
<https://tier4.atlassian.net/wiki/spaces/CT/pages/3043098868/WIP+Perception+ECU+setup+for+the+bench+environment#camera-driver-installation.1>

<!-- markdown-link-check-disable -->

<!-- markdown-link-check-enable -->

### Remarks
