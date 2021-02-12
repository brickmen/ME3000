# Highbanks ME3000

SLAVE=0x01
THRESHOLD_FILE="pct.txt"
SERIAL_PORT="/dev/ttyUSB2"
MIN_CHARGE=20
MAX_CHARGE=99

# MQTT
ME3000_NAME='me3000'
MQTT_HOST='localhost'
MQTT_USER='solarMODBUS'
MQTT_PWD='solar'

TOPICS = ((6, 'voltage', 'H'),
          (7, 'current', 'h'),
          (14, 'batt_voltage', 'H'),
          (15, 'batt_current', 'h'),
          (16, 'batt_capacity', 'H'),
          (17, 'batt_temp', 'H'),
          (25, 'sell_grid', 'H'),
          (26, 'buy_grid', 'H'),
          (27, 'load_use', 'H'),
          (36, 'charge_total', 'H'),
          (37, 'discharge_total', 'H')
         )
  
