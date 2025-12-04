# link retry handler

【Anvil向け】このRoleでは、Anvilの10GbEポートがECU起動時に通信できない事象に対する対策を実施します。

## Role in system design

link retry handlerはnetworkd-dispatcherを用いて、当該ポートの接続先と疎通確認を実施し、疎通できなかった場合に当該ポートのLink Down/Upを実施する。

## Dependency

## Usage

### Variables

| Variables                       | default value | description            |
| ------------------------------- | ------------- | ---------------------- |
| link_retry_handler_ping_dst_ip  | 192.168.30.11 | 疎通確認先のIPアドレス |
| link_retry_handler_network_port | mgbe1         | 当該の10GbEポート名    |

### Preparation

playbook への追加例

```yaml
- { role: link_retry_handler, tags: [link_retry_handler] }
```

## Related links

<https://tier4.atlassian.net/browse/RT0-31958>

### Remarks
