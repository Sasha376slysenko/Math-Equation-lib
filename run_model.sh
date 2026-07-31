#!/bin/bash

GREEN='\033[0;32m'
BLUE='\033[0;36m'
ORANGE='\033[38;5;208m'
NC='\033[0;0m'

OS_TYPE="$(UNAME -S)"

if [ "$OS_TYPE" = "Linux" ]; then
  RAPL_FILE='/sys/class/powercap/intel-rapl/intel-rapl:0/energy_uj'

  if [ -f "$RAPL_FILE" ] && [ ! -r "$RAPL_FILE" ]; then
    echo -e "${ORANGE}[INFO] Надаємо доступ до апаратних лічильників RAPL${NC}"
    sudo chmod -R a+r /sys/class/powercap/intel-rapl
  fi
  RUN_CMD="PYTHONPATH=. python modeling/main.py"
elif [ "$OS_TYPE" = "Darwin" ]; then
  echo -e "${ORANGE}[INFO macOS] Запуск із sudo для доступу до апаратних лічильників ${NC}"
  RUN_CMD="sudo -E env \"PATH=$PATH\" \"PYTHONPATH=.\" python modeling/main.py"
else
  RUN_CMD="PYTHONPATH=. python modeling/main.py"
fi

echo -e "${GREEN} [START] Model${NC}"

eval $RUN_CMD

echo -e "${BLUE} [END] Model${NC}"
