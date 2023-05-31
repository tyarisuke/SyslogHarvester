import subprocess
from abc import ABC, abstractmethod

class LogCollectorABC(ABC):
    """An abstract base class for fetching system logs."""

    @abstractmethod
    def __init__(self, **options):
        pass

    @abstractmethod
    def get_output(self):
        pass


class SyslogHarvester(LogCollectorABC):
    """A class for fetching system logs via the `journalctl` command."""

    def __init__(self, **options):
        """
        Initialize the harvester with optional arguments for the `journalctl` command.
        
        Args:
            **options: Variable length argument list of options for the `journalctl` command.
        """
        self.options = options

    def _build_command(self):
        """
        Build the `journalctl` command with the given options.
        
        Returns:
            list: The command as a list of strings.
        """
        command = ['journalctl']
        for option, value in self.options.items():
            command.append(f'--{option}')
            if value is not None:
                command.append(str(value))
        return command

    def get_output(self):
        """
        Execute the `journalctl` command with the given options and return its output.
        
        Returns:
            str: The output of the `journalctl` command, or None if an error occurred.
        """
        command = self._build_command()

        # Execute the command and capture the output
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0:
            print(f'Error: {result.stderr.decode()}')
            return None

        return result.stdout.decode()
