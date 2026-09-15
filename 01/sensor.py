import signal
import sys
import time

# Обработчик сигнала SIGINT (Ctrl + C)
# SIG_DFL – дефолтный обработчик ядра ОС (для каждого сигнала свои действия)
# Дефолт для SIGINT – убийство процесса
# Если обработчик не ставить, Python для SIGINT ведет себя иначе
signal.signal(signal.SIGINT, signal.SIG_DFL)

# читаем любую строку; используется просто для отображения
sensor_name = sys.stdin.readline().strip()
if not sensor_name:
  print("ERROR: sensor name is missing", file=sys.stderr, flush=True)
  sys.exit(2)

tick = 1
while True:
  # просто печатаем каждую секунду в поток вывода
  print(f"INFO {sensor_name} tick={tick}", flush=True)

  if tick % 5 == 0:
    # каждую пятую секунду печатаем в поток ошибок
    print(
      f"WARN {sensor_name} tick={tick} simulated warning",
      file=sys.stderr,
      flush=True,
    )

  time.sleep(1)
  tick += 1

