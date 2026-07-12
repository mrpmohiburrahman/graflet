[Changelog](https://freemius.com/changelog/) / New security system to prevent card testing attacks

Over the past few weeks, we’ve gradually been rolling out a new system to identify and block card testing attempts. We already had a system like this in place, but after a few recent attacks, we recognized it needed a complete overhaul to work more intelligently.

Our CTO, [Dror Yaakov](https://www.linkedin.com/in/droryaakov/?originalSubdomain=il), has been leading the development of this system. To test its effectiveness, we ran it in “observation” mode over the past few weeks. After gathering enough data and proving its effectiveness, we’re finally letting it out at full capacity. Our hope is that it will better serve our partners to detect attacks and prevent financial losses.

## From under the hood

While developing this system, we combined our collective years of experience to come up with the best possible strategies. We learned many things in the process.

### Redundancy is good

An attacker is usually smart enough to rotate a large set of emails and IP addresses, among other things. Tracking just one or a few of them is usually not enough. We’ve found that the more redundant the system, the better it is at detecting such parameters.

### reCAPTCHA can be bypassed

While Google reCAPTCHA is no doubt an excellent tool to prevent automated submissions, we’ve found it can be bypassed, although this doesn’t come easy or cheap. Relying on reCAPTCHA alone as the ultimate security measure is almost never enough. It’s better to have a two-factor authentication system where real human intervention is always required.

### Traffic monitoring works best when everything else fails

A very sophisticated attack can fool even a very strong system. In such cases, having another redundant system to monitor traffic and spikes helps a lot with identifying such attacks.

* * *

The above are only a few of the strategies our new system implements. We hope it gives your users a better checkout experience. If you face any issues, please don’t hesitate to contact us at [\[email protected\]](https://freemius.com/cdn-cgi/l/email-protection#87f4f2f7f7e8f5f3c7e1f5e2e2eaeef2f4a9e4e8ea).