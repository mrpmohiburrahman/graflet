---
title: "Utilizing semantic versioning in Release Management"
url: "https://freemius.com/help/documentation/release-management/semantic-versioning/"
source: "docs"
section: "Docs"
category: "Release Management"
scraped_at: "2026-04-09T19:58:40+06:00"
word_count: 199
---

Freemius supports a variation of [Semantic Versioning 2.0.0](https://semver.org/): `major.minor[.patch[-pre_major[.pre_minor[.pre_patch]]]][+metadata]`

Given a version number `major.minor.patch`, increment the:

- `major` version when you make incompatible API changes,
- `minor` version when you add functionality in a backwards compatible manner, and
- `patch` version when you make backwards compatible bug fixes.
- A pre-release version may be denoted by appending a hyphen (`-`) and a series of dot separated identifiers immediately following the patch version. Identifiers **must** comprise only ASCII alphanumerics and hyphens `[0-9A-Za-z-]`. Identifiers **must not** be empty. Numeric identifiers **must not** include leading zeroes. Pre-release versions have a lower precedence than the associated normal version. A pre-release version indicates that the version is unstable and might not satisfy the intended compatibility requirements as denoted by its associated normal version. Examples:
  
  - `1.0.0-alpha`,
  - `1.0.0-alpha.1`,
  - `1.0.0-0.3.7`,
  - `1.0.0-x.7.z.92`.
- Build `metadata` **must** comprise only ASCII alphanumerics and hyphens `[0-9A-Za-z-]`.

Valid version examples:

- `1.2.7-alpha`
- `1.2.7-alpha.1`
- `1.2.7-beta`
- `1.2.7-rc.2`
- `1.2.7`
- `1.2.8-rc.1+20210411`

Important versions hirerachy:

- `1.2-beta` &lt; `1.2` &lt; `1.2.0` &lt; `1.2.1` &lt; `1.2.2` &lt; `1.2.10`
- `1.2.7-alpha` &lt; `1.2.7-alpha.1` &lt; `1.2.7-beta` &lt; `1.2.7-rc.2` &lt; `1.2.7`
- `1.2+20210411` == `1.2+whatever`
- `1.2.7-RC` &lt; `1.2.7.rc` ([ASCII('UPPERCASE') &lt; ASCII('lowercase')](http://www.asciitable.com/))