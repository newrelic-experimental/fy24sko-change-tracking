<a href="https://opensource.newrelic.com/oss-category/#new-relic-experimental"><picture><source media="(prefers-color-scheme: dark)" srcset="https://github.com/newrelic/opensource-website/raw/main/src/images/categories/dark/Experimental.png"><source media="(prefers-color-scheme: light)" srcset="https://github.com/newrelic/opensource-website/raw/main/src/images/categories/Experimental.png"><img alt="New Relic Open Source experimental project banner." src="https://github.com/newrelic/opensource-website/raw/main/src/images/categories/Experimental.png"></picture></a>

# FY24SKO-Change-Tracking

This is a hands-on, self-paced lab that teaches students how to use New Relic Change Tracking markers with GitHub Actions, the NerdGraph API, and the New Relic CLI.

*Based on the [sample application](https://github.com/newrelic/go-agent/blob/master/v3/examples/server/main.go) in the New Relic Go Agent repository*

## Background

Tracking changes across your systems is a fundamental practice in your Observability journey for a number of reasons such as:
 * Debugging and troubleshooting: When something goes wrong, it's critical to know what changed recently in order to reduce your mean time to resolution (MTTR).
 * Collaboration: As distributed teams work together, it's important to track changes and ensure everyone has a single source of truth where they can manage the impact of their changes together seamlessly.
 * Version control: Keeping track of when versions are deployed allows greater flexibility and speed for rolling back when unexpected situations arise, or isolating telemetry during things like A/B testing.
 * Compliance and auditing: In many industries, tracking changes is a requirement of various standards which allows auditors to trace changes back to their owning teams with ease.

Learn more about New Relic Change Tracking in [our documentation](https://docs.newrelic.com/docs/change-tracking/change-tracking-introduction/).

## Installation

This lab is intended to be almost entirely completed in your browser, with the exception of the segment on using the [New Relic CLI](/lab_guide/4_NEW%20RELIC%20CLI.md). As such, you will primarily be working in your own fork of this repository and you should not need to create a local clone or host anything on your own laptop.

## Getting Started

All steps required to completed this lab are in the `/lab_guide` directory, outlined below:

### Lab Sections

 * [Introduction](/lab_guide/1_INTRO.md)
 * [GitHub Action](/lab_guide/2_GITHUB%20ACTION.md)
 * [NerdGraph API](/lab_guide/3_NERDGRAPH%20API.md)
 * [New Relic CLI](/lab_guide/4_NEW%20RELIC%20CLI.md)
 * [Conclusion](/lab_guide/5_CONCLUSION.md)

## Contributing

We encourage your contributions to improve **FY24SKO-Change-Tracking**! Keep in mind when you submit your pull request, you'll need to sign the CLA via the click-through using CLA-Assistant. You only have to sign the CLA one time per project.
If you have any questions, or to execute our corporate CLA, required if your contribution is on behalf of a company,  please drop us an email at opensource@newrelic.com.

**A note about vulnerabilities**

As noted in our [security policy](../../security/policy), New Relic is committed to the privacy and security of our customers and their data. We believe that providing coordinated disclosure by security researchers and engaging with the security community are important means to achieve our security goals.

If you believe you have found a security vulnerability in this project or any of New Relic's products or websites, we welcome and greatly appreciate you reporting it to New Relic through [HackerOne](https://hackerone.com/newrelic).

## License

**FY24SKO-Change-Tracking** is licensed under the [Apache 2.0](http://apache.org/licenses/LICENSE-2.0.txt) License.
