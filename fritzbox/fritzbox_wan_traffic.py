import datetime
from fritzconnection import FritzConnection
from influxdb import InfluxDBClient


def get_json(measurement, value, host, direction, value_type):
    current_datetime = datetime.datetime.now().isoformat()
    json_body_template = {
        "measurement": measurement,
        "tags": {
            "host": host,
            "direction": direction,
            "type": value_type
        },
        "time": current_datetime,
        "fields": {
            "value": value
        }
    }
    return json_body_template


def get_values():
    try:
        conn = FritzConnection(address='192.168.178.1')
    except Exception as e:
        print("cannot connect to fritzbox")

    info = conn.call_action('WANCommonIFC', 'GetAddonInfos')

    collection = []

    currentDownstream = info["NewByteReceiveRate"]
    collection.append(get_json("WANTraffic", currentDownstream, "fritzbox", "down", "current"))
    currentUpstream = info["NewByteSendRate"]
    collection.append(get_json("WANTraffic", currentUpstream, "fritzbox", "up", "current"))
    totalDownstream = int(info["NewX_AVM_DE_TotalBytesReceived64"])
    collection.append(get_json("WANTraffic", totalDownstream, "fritzbox", "down", "total"))
    totalUpstream =  int(info["NewX_AVM_DE_TotalBytesSent64"])
    collection.append(get_json("WANTraffic", totalUpstream, "fritzbox", "up", "total"))

    return collection


values = get_values()
print(values)

client = InfluxDBClient('192.168.178.3', 8086, '', '', 'perf_stats')
client.write_points(values)