#!/usr/bin/env python3
"""
Filtered logger module
"""

import re
import logging
from typing import List


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """
    Returns the log message obfuscated.
    """
    for field in fields:
        message = re.sub(
            f"{field}=[^{separator}]*",
            f"{field}={redaction}",
            message)
    return message


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Create a new instance of RedactingFormatter.

        Args:
            fields (List[str]): A list of strings representing
            fields to obfuscate.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Filter values in incoming log records using filter_datum.

        Args:
            record (logging.LogRecord): The log record.

        Returns:
            str: The formatted and obfuscated log record.
        """
        original_formatted_message = super().format(record)
        return filter_datum(
            self.fields,
            self.REDACTION,
            original_formatted_message,
            self.SEPARATOR)
