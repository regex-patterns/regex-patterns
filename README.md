
# Regex Patterns

<p align="center">
  <a href="/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg"/></a>
  <!-- <img alt="PyPI - Downloads" src="https://pepy.tech/badge/commonregex-improved/month"> -->
   <img alt="PyPI - Downloads" src="https://pepy.tech/badge/commonregex-improved">
   <a href="https://twitter.com/brootware"><img src="https://img.shields.io/twitter/follow/brootware?style=social" alt="Twitter Follow"></a>
   <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/commonregex-improved"> <img alt="PyPI" src="https://img.shields.io/pypi/v/commonregex-improved">
   <a href="https://sonarcloud.io/summary/new_code?id=brootware_commonregex-improved"><img src="https://sonarcloud.io/api/project_badges/measure?project=brootware_commonregex-improved&metric=alert_status" alt="reliability rating"></a>
   <img alt="GitHub Workflow Status" src="https://img.shields.io/github/workflow/status/brootware/commonregex-improved/ci.yml?branch=main">
</p>

<p align="center">
  An improved version of commonly used regular expressions in Python
</p>

<br><br>

> Inspired by and improved upon:
> - [CommonRegex](https://github.com/madisonmay/CommonRegex)
> - [CommonRegex Improved](https://github.com/brootware/commonregex-improved)

This is a collection of commonly used regular expressions. This library provides a simple API interface to match the strings corresponding to specified patterns.

## Installation

```bash
pip install --upgrade regex-patterns
```

## Usage 

```python
from regex_patterns import RegexPatterns

patterns = RegexPatterns()

text = (
    "John, please get that article on www.linkedin.com to me by 5:00PM on Jan 9th 2012. "
    "4:00 would be ideal, actually or 5:30 P.M. If you have any questions, You can "
    "reach me at (519)-236-2723x341 or get in touch with my associate at "
    "harold_smith@gmail.com. You can find my ip address at 127.0.0.1 or at "
    "64.248.67.225. I also have a secret protected with md5 "
    "8a2292371ee60f8212096c06fe3335fd. The internal webpage to get the article from is "
    "https://internal.sharepoint.edu.au"
)

date_list = patterns.dates(text)
# ['Jan 9th 2012']
time_list = patterns.times(text)
# ['5:00pm', '4:00 ', '5:30 P.M.']
url_list = patterns.links(text)
# ['www.linkedin.com', 'gmail.com', 'https://internal.sharepoint.edu.au']
phone_list = patterns.phones_with_exts(text)  
# ['(519)-236-2723x341']
ip_list = patterns.ips(text)
# ['127.0.0.1', '64.248.67.225']
email_list = patterns.emails(text)
# ['harold_smith@gmail.com']
md5_list = patterns.md5_hashes(text)
# ['8a2292371ee60f8212096c06fe3335fd']
```

## Features / Supported Methods

* `dates(text: str)`
* `times(text: str)`
* `phones(text: str)`
* `phones_with_exts(text: str)`
* `links(text: str)`
* `emails(text: str)`
* `ipv4s(text: str)`
* `ipv6s(text: str)`
* `ips(text: str)`
* `not_known_ports(text: str)`
* `prices(text: str)`
* `hex_colors(text: str)`
* `credit_cards(text: str)`
* `visa_cards(text: str)`
* `master_cards(text: str)`
* `btc_address(text: str)`
* `street_addresses(text: str)`
* `zip_codes(text: str)`
* `po_boxes(text: str)`
* `ssn_numbers(text: str)`
* `md5_hashes(text: str)`
* `sha1_hashes(text: str)`
* `sha256_hashes(text: str)`
* `isbn13s(text: str)`
* `isbn10s(text: str)`
* `mac_addresses(text: str)`
* `iban_numbers(text: str)`
* `git_repos(text: str)`
