"""Unit tests that never connect to a real network service."""
import contextlib
import io
import unittest
from unittest.mock import MagicMock, patch

import scanner


class ScannerTests(unittest.TestCase):
    @patch("scanner.socket.socket")
    def test_open_and_closed_ports(self, socket_factory):
        sock = MagicMock()
        socket_factory.return_value.__enter__.return_value = sock
        sock.connect_ex.side_effect = [0, 111, 0, 111, 111, 111, 111]
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            scanner.main()
        lines = output.getvalue()
        self.assertIn("Port 21: OPEN", lines)
        self.assertIn("Port 22: Not open or unreachable", lines)
        self.assertEqual(sock.connect_ex.call_count, len(scanner.PORTS))
        self.assertTrue(all(call.args[0][0] == "127.0.0.1" for call in sock.connect_ex.call_args_list))
        self.assertEqual(sock.settimeout.call_count, len(scanner.PORTS))


if __name__ == "__main__":
    unittest.main()
