# Node Monitoring

As a node operator, it is important to monitor the performance and availability of your nodes to ensure that they are
operating correctly. Monitoring your nodes can help you identify issues before they become critical and take action to
resolve them.

## Uptime monitoring

The first category of tools we recommend using are uptime monitoring tools. These tools will notify you if your node
becomes unavailable, allowing you to take action to resolve the issue.

Some examples of uptime monitoring tools include:

| Software | URL | Licence | Open-Source |
| --- | --- | --- | --- |
| Uptime Kuma | [https://uptime.kuma.pet/](https://uptime.kuma.pet/) | MIT | Yes |
| Upptime | [https://upptime.js.org/](https://upptime.js.org/) | MIT | Yes |
| UptimeRobot | [https://uptimerobot.com/](https://uptimerobot.com/) | Proprietary | No |

This list is not exhaustive, and there are many other uptime monitoring tools available.

The main endpoints to monitor are:

 - On Core Channel Nodes (CCN): `/metrics`
 - On Compute Resource Nodes (CRN): `/status/check/fastapi`

Examples:

- Aleph CCN: [https://official.aleph.cloud/metrics](https://api2.aleph.im/metrics)
- Aleph Staging CRN: [https://ovh.staging.aleph.sh/status/check/fastapi](https://ovh.staging.aleph.sh/status/check/fastapi)

## Resource monitoring

The second category of tools we recommend using are resource monitoring tools. These tools will allow you to monitor the
resource usage of your nodes, such as CPU, memory, and disk usage. Monitoring these metrics can help you identify
performance issues before they become critical.

Some examples of resource monitoring tools include:

| Software | URL | Licence | Open-Source |
| --- | --- | --- | --- |
| Prometheus | [https://prometheus.io/](https://prometheus.io/) | Apache 2.0 | Yes |
| Grafana | [https://grafana.com/](https://grafana.com/) | Apache 2.0 | Yes |
| Netdata | [https://www.netdata.cloud/](https://www.netdata.cloud/) | GPL v3 | Yes |

These can be hosted on your own infrastructure or used as services provided by third parties.

Again, this list is not exhaustive, and there are many other resource monitoring tools available.

## Node metrics

Measurements of the performance and reliability of the nodes are published in the form of 
[POST messages](../../protocol/object-types/posts.md) to the Aleph.im network. See the [Metrics](./metrics.md) page for more information.

You can find [the metrics and scoring messages on the Explorer](https://explorer.aleph.im/messages?showAdvancedFilters=1&channels=aleph-scoring&page=1&sender=0x4D52380D3191274a04846c89c069E6C3F2Ed94e4).

The last two weeks of metrics of a specific node can be fetched from any Core Channel Node (CCN) by using the following
endpoint: 

 - For Core Channel Nodes: `/api/v0/core/${node.hash}/metrics`
 - For Compute Resource Nodes: `/api/v0/compute/${node.hash}/metrics`

Examples: 

 - [https://official.aleph.cloud/api/v0/core/6c7578899ac475fbdc05c6a4711331c7590aa6b719f0c169941b99a10faf1136/metrics](https://official.aleph.cloud/api/v0/core/6c7578899ac475fbdc05c6a4711331c7590aa6b719f0c169941b99a10faf1136/metrics)
 - [https://official.aleph.cloud/api/v0/compute/ec6ff7010de501b292333f390a46a227e349de6425fde4bd47d06ade82d3786c/metrics](https://official.aleph.cloud/api/v0/compute/ec6ff7010de501b292333f390a46a227e349de6425fde4bd47d06ade82d3786c/metrics)

Additionally, the index page of Compute Resource Nodes provides a small graph that displays the values of these metrics
after pressing the button "_Load metrics chart_" :

![CRN metrics graph](metrics-visualizer.png)