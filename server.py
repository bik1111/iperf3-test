#!/usr/bin/env python3

import iperf3
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--ip', required=True)
parser.add_argument('--port', required=False, default=5201)
args = parser.parse_args()

server = iperf3.Server()
print("server", server)
server.bind_address = str(args.ip)
server.port = int(args.port)

print('Running server: {0}:{1}'.format(server.bind_address, server.port))
print("111")
while True:
    print("11")
    result = server.run()

    if result.error:
        print(result.error)
    else:
        print('')
        print('Test results from {0}:{1}'.format(result.remote_host,
                                                 result.remote_port))
        print('  started at         {0}'.format(result.time))
        print('  bytes received     {0}'.format(result.received_bytes))

        print('Average transmitted received in all sorts of networky formats:')
        print('  bits per second      (bps)   {0}'.format(result.received_bps))
        print('  Kilobits per second  (kbps)  {0}'.format(result.received_kbps))
        print('  Megabits per second  (Mbps)  {0}'.format(result.received_Mbps))
        print('  KiloBytes per second (kB/s)  {0}'.format(result.received_kB_s))
        print('  MegaBytes per second (MB/s)  {0}'.format(result.received_MB_s))
        print('')
        break


