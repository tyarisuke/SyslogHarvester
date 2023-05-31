# SyslogHarvester

SyslogHarvester is a Python tool for fetching system logs via the `journalctl` command. It provides a flexible interface for retrieving logs with various options. It's ideal for debugging and monitoring system logs.

## Features

- Fetch system logs via `journalctl`.
- Provides various options for `journalctl`.

## Installation

You can install SyslogHarvester by cloning this repository:

```bash
git clone https://github.com/yourusername/syslogharvester.git
```
## Usage

Here is a basic example of using SyslogHarvester

```python
from syslogharvester import SyslogHarvester

# Initialize harvester with options
harvester = SyslogHarvester(boot=True, unit='nginx.service')

# Get output
output = harvester.get_output()

# Print output
print(output)

```

## License
SyslogHarvester is licensed under the terms of the MIT License. See LICENSE for more information.
