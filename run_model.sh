#!/bin/bash

GREEN='\033[0;32m'
BLUE='\033[0;36m'
ORANGE='\033[38;5;208m'
NC='\033[0;0m'

RAPL_FILE='/sys/class/powercap/intel-rapl/intel-rapl:0/energy_uj'

if [ -f "$RAPL_FILE" ] && [ ! -r "$RAPL_FILE" ]; then
  echo -e "${ORANGE}[INFO] Надаємо доступ до апаратних лічильників RAPL${NC}"
  sudo chmod -R a+r /sys/class/powercap/intel-rapl
fi

echo -e "${GREEN} [START] Model${NC}"

PYTHONPATH=. python modeling/main.py

echo -e "${BLUE} [END] Model${NC}"
