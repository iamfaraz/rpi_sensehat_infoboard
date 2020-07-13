#!/usr/bin/env python3

from sense_hat import SenseHat
import time
import math
import os
from subprocess import check_output

"""

  Sense HAT Sensors Display

  Select Temperature, Pressure, or Humidity  with the Joystick
  to visualize the current sensor values on the LED.

  Note: Requires sense_hat 2.2.0 or later

"""

sense = SenseHat()

green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
l_blue = (51, 204, 255)
lush_green = (0, 100, 67)
warning_color = (255, 204, 0)
danger_color = (204, 0, 0)
temp_color = (51, 204, 255)
current_temp = 0
global test_var

def digit_T(color):
  X = color
  O = [0, 0, 0]
  return [
    O,O,O,O,O,O,O,O,
    O,X,X,X,X,X,X,O,
    O,X,X,X,X,X,X,O,
    O,O,O,X,X,O,O,O,
    O,O,O,X,X,O,O,O,
    O,O,O,X,X,O,O,O,
    O,O,O,X,X,O,O,O,
    O,O,O,O,O,O,O,O
  ]

def digit_R(color):
  X = color
  O = [0, 0, 0]
  return [
    O,O,O,O,O,O,O,O,
    O,X,X,X,X,X,O,O,
    O,X,X,O,O,X,X,O,
    O,X,X,O,O,X,X,O,
    O,X,X,X,X,O,O,O,
    O,X,X,O,X,X,O,O,
    O,X,X,O,O,X,X,O,
    O,O,O,O,O,O,O,O
  ]

def digit_Reboot(color):
  X = color
  O = [0, 0, 0]
  return [
    O,O,O,O,O,O,O,O,
    O,O,X,X,X,O,X,O,
    O,X,O,O,O,X,X,O,
    O,X,O,O,X,X,X,O,
    O,X,O,O,O,O,O,O,
    O,X,O,O,O,X,O,O,
    O,O,X,X,X,O,O,O,
    O,O,O,O,O,O,O,O
  ]

def digit_Shutdown(color):
  X = color
  O = [0, 0, 0]
  return [
    O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O
  ]

def digit_P(color):
  X = color
  O = [0, 0, 0]
  return [
    O,O,O,O,O,O,O,O,
    O,X,X,X,X,X,X,O,
    O,X,X,O,O,X,X,O,
    O,X,X,O,O,X,X,O,
    O,X,X,X,X,X,X,O,
    O,X,X,O,O,O,O,O,
    O,X,X,O,O,O,O,O,
    O,O,O,O,O,O,O,O
  ]

def digit_H(color):
  X = color
  O = [0, 0, 0]
  return [
    O,O,O,O,O,O,O,O,
    O,X,X,O,O,X,X,O,
    O,X,X,O,O,X,X,O,
    O,X,X,X,X,X,X,O,
    O,X,X,X,X,X,X,O,
    O,X,X,O,O,X,X,O,
    O,X,X,O,O,X,X,O,
    O,O,O,O,O,O,O,O
  ]

def digit_Cl(color):
  X = color
  O = [0, 0, 0]
  return [
    X,X,O,X,O,O,X,X,
    X,O,O,X,O,O,X,X,
    X,X,O,X,X,O,X,X,
    O,O,O,O,O,O,O,O,
    X,X,X,O,X,O,X,O,
    X,O,O,O,X,X,O,O,
    X,X,X,O,X,O,X,O,
    O,O,O,O,O,O,O,O
  ]

def digit_C(color):
  X = color
  O = [0, 0, 0]
  return [
    O,O,O,O,O,O,O,O,
    O,X,X,X,X,X,X,O,
    O,X,X,X,X,X,X,O,
    O,X,X,O,O,O,O,O,
    O,X,X,O,O,O,O,O,
    O,X,X,X,X,X,X,O,
    O,X,X,X,X,X,X,O,
    O,O,O,O,O,O,O,O
  ]


def digit_IP(color):
  X = color
  O = [0, 0, 0]
  return [
    O,O,O,O,O,O,O,O,
    O,X,O,X,X,X,X,O,
    O,X,O,X,O,O,X,O,
    O,X,O,X,O,O,X,O,
    O,X,O,X,X,O,X,O,
    O,X,O,X,O,O,O,O,
    O,X,O,X,O,O,O,O,
    O,O,O,O,O,O,O,O
  ]

def digit_clock(color1, color2):
  X = color1
  Y = color2
  O = [0, 0, 0]
  return [
    X,X,O,O,X,X,X,O,
    O,O,X,O,O,O,X,O,
    O,X,O,O,O,X,O,O,
    X,Y,Y,Y,O,Y,X,Y,
    X,X,X,O,X,X,O,Y,
    O,Y,Y,Y,O,O,Y,O,
    O,O,O,Y,O,Y,O,O,
    O,Y,Y,O,O,Y,O,O
  ]



def digit_b(color):
  X = color
  O = [0, 0, 0]
  return [
    O,O,O,O,
    O,O,O,O,
    O,O,O,O,
    O,O,O,O,
    O,O,O,O,
    O,O,O,O,
    O,O,O,O,
    O,O,O,O
  ]

def digit_1(color):
  X = color
  O = [0, 0, 0]
  return [
    O,O,O,O,
    O,X,O,O,
    X,X,O,O,
    O,X,O,O,
    O,X,O,O,
    O,X,O,O,
    X,X,X,O,
    O,O,O,O
  ]

def digit_2(color):
  X = color
  O = [0, 0, 0]
  return [
    O,O,O,O,
    X,X,O,O,
    O,O,X,O,
    O,X,O,O,
    X,X,O,O,
    X,O,O,O,
    X,X,X,O,
    O,O,O,O
  ]

def digit_3(color):
  X = color
  O = [0, 0, 0]
  return [
    O,O,O,O,
    X,X,O,O,
    O,O,X,O,
    O,X,X,O,
    O,X,X,O,
    O,O,X,O,
    X,X,O,O,
    O,O,O,O
  ]

def digit_4(color):
  X = color
  O = [0, 0, 0]
  return [
    O,O,O,O,
    X,O,X,O,
    X,O,X,O,
    X,X,X,O,
    O,O,X,O,
    O,O,X,O,
    O,O,X,O,
    O,O,O,O
  ]

def digit_5(color):
  X = color
  O = [0, 0, 0]
  return [
    O,O,O,O,
    X,X,X,O,
    X,O,O,O,
    X,X,O,O,
    O,X,X,O,
    O,O,X,O,
    X,X,O,O,
    O,O,O,O
  ]

def digit_6(color):
  X = color
  O = [0, 0, 0]
  return [
    O,O,O,O,
    O,X,X,O,
    X,O,O,O,
    X,X,O,O,
    X,O,X,O,
    X,O,X,O,
    O,X,O,O,
    O,O,O,O
  ]

def digit_7(color):
  X = color
  O = [0, 0, 0,]
  return [
    O,O,O,O,
    X,X,X,O,
    O,O,X,O,
    O,O,X,O,
    O,X,O,O,
    O,X,O,O,
    O,X,O,O,
    O,O,O,O
  ]

def digit_8(color):
  X = color
  O = [0, 0, 0,]
  return [
    O,O,O,O,
    X,X,X,O,
    X,O,X,O,
    X,X,X,O,
    X,X,X,O,
    X,O,X,O,
    X,X,X,O,
    O,O,O,O
  ]

def digit_9(color):
  X = color
  O = [0, 0, 0,]
  return [
    O,O,O,O,
    X,X,X,O,
    X,O,X,O,
    X,X,X,O,
    O,O,X,O,
    O,O,X,O,
    X,X,X,O,
    O,O,O,O
  ]

def digit_0(color):
  X = color
  O = [0, 0, 0,]
  return [
    O,O,O,O,
    O,X,O,O,
    X,O,X,O,
    X,O,X,O,
    X,O,X,O,
    X,O,X,O,
    O,X,O,O,
    O,O,O,O
  ]

def sdigit_b(color):
  X = color
  O = [0, 0, 0]
  return [
    O,O,O,O,
    O,O,O,O,
    O,O,O,O,
    O,O,O,O
  ]

def sdigit_1(color):
  X = color
  O = [0, 0, 0]
  return [
    O,O,O,X,
    O,O,X,X,
    O,O,O,X,
    O,O,O,X
  ]

def sdigit_2(color):
  X = color
  O = [0, 0, 0]
  return [
    O,X,X,X,
    O,O,X,X,
    O,X,X,O,
    O,X,X,X
  ]

def sdigit_3(color):
  X = color
  O = [0, 0, 0]
  return [
    O,X,X,X,
    O,O,X,X,
    O,O,O,X,
    O,X,X,X
  ]

def sdigit_4(color):
  X = color
  O = [0, 0, 0]
  return [
    O,X,O,X,
    O,X,O,X,
    O,X,X,X,
    O,O,O,X
  ]

def sdigit_5(color):
  X = color
  O = [0, 0, 0]
  return [
    O,X,X,X,
    O,X,X,O,
    O,O,X,X,
    O,X,X,X
  ]

def sdigit_6(color):
  X = color
  O = [0, 0, 0]
  return [
    O,X,O,O,
    O,X,X,X,
    O,X,O,X,
    O,X,X,X
  ]

def sdigit_7(color):
  X = color
  O = [0, 0, 0,]
  return [
    O,X,X,X,
    O,O,O,X,
    O,O,X,O,
    O,O,X,O
  ]

def sdigit_8(color):
  X = color
  O = [0, 0, 0,]
  return [
    O,X,X,O,
    O,X,X,X,
    O,X,O,X,
    O,X,X,X
  ]

def sdigit_9(color):
  X = color
  O = [0, 0, 0,]
  return [
    O,X,X,X,
    O,X,O,X,
    O,X,X,X,
    O,O,O,X
  ]

def sdigit_0(color):
  X = color
  O = [0, 0, 0,]
  return [
    O,O,X,O,
    O,X,O,X,
    O,X,O,X,
    O,O,X,O
  ]

def get_digit_map(large, digit, color):
  if large:
    if digit == 0:
      return digit_0(color)
    elif digit == 1:
      return digit_1(color)
    elif digit == 2:
      return digit_2(color)
    elif digit == 3:
      return digit_3(color)
    elif digit == 4:
      return digit_4(color)
    elif digit == 5:
      return digit_5(color)
    elif digit == 6:
      return digit_6(color)
    elif digit == 7:
      return digit_7(color)
    elif digit == 8:
      return digit_8(color)
    elif digit == 9:
      return digit_9(color)
    else:
      return digit_b(color)
  else:
    if digit == 0:
      return sdigit_0(color)
    elif digit == 1:
      return sdigit_1(color)
    elif digit == 2:
      return sdigit_2(color)
    elif digit == 3:
      return sdigit_3(color)
    elif digit == 4:
      return sdigit_4(color)
    elif digit == 5:
      return sdigit_5(color)
    elif digit == 6:
      return sdigit_6(color)
    elif digit == 7:
      return sdigit_7(color)
    elif digit == 8:
      return sdigit_8(color)
    elif digit == 9:
      return sdigit_9(color)
    else:
      return sdigit_b(color)

# compose an image of 2 upper digits and 2 lower digits
def compose_image(U1, U2):
  image = []
  image[0:7] = U1[0:4] + U2[0:4]
  image[8:15] = U1[4:8] + U2[4:8]
  image[16:23] = U1[8:12] + U2[8:12]
  image[24:31] = U1[12:16] + U2[12:16]
  image[32:39] = U1[16:20] + U2[16:20]
  image[40:47] = U1[20:24] + U2[20:24]
  image[48:55] = U1[24:28] + U2[24:28]
  image[56:63] = U1[28:32] + U2[28:32]
  return image

def display_digits(value, color):
    value = math.trunc(value)
    U1 = get_digit_map(True, value // 10, color)
    U2 = get_digit_map(True, value % 10, color)
    return compose_image(U1, U2)

def display_clock(hours, minutes):
  upper_color = lush_green
  lower_color = [100, 0, 33]

  U1 = get_digit_map(False, hours // 10, upper_color)
  U2 = get_digit_map(False, hours % 10, upper_color)
  L1 = get_digit_map(False, minutes // 10, lower_color)
  L2 = get_digit_map(False, minutes % 10, lower_color)
  sense.set_pixels(compose_4x4image(U1, U2, L1, L2))

def compose_4x4image(U1, U2, L1, L2):
  image = []
  image[0:7] = U1[0:4] + U2[0:4]
  image[8:15] = U1[4:8] + U2[4:8]
  image[16:23] = U1[8:12] + U2[8:12]
  image[24:31] = U1[12:16] + U2[12:16]

  image[32:39] = L1[0:4] + L2[0:4]
  image[40:47] = L1[4:8] + L2[4:8]
  image[48:55] = L1[8:12] + L2[8:12]
  image[56:63] = L1[12:16] + L2[12:16]
  return image

def show_t(color):
    sense.set_pixels(digit_T(color))
    #sense.show_letter("T", back_colour = red)
    time.sleep(.25)

def show_p():
    sense.set_pixels(digit_P(green))
    #sense.show_letter("P", back_colour = green)
    time.sleep(.25)

def show_h():
    sense.set_pixels(digit_H(blue))
    time.sleep(.25)

def show_c():
    sense.set_pixels(digit_C((204, 0, 204)))
    time.sleep(.25)
    
def show_cl():
    sense.set_pixels(digit_Cl(lush_green))
    time.sleep(.25)

def show_ip():
    sense.set_pixels(digit_IP((153, 102, 51)))
    time.sleep(.25)

def show_r():
    sense.set_pixels(digit_R((0, 255, 204)))
    time.sleep(.25)

# get CPU temperature
def get_cpu_temp():
  res = os.popen("vcgencmd measure_temp").readline()
  t = float(res.replace("temp=","").replace("'C\n",""))
  return(t)

# use moving average to smooth readings
def get_smooth(x):
  if not hasattr(get_smooth, "t"):
    get_smooth.t = [x,x,x]
  get_smooth.t[2] = get_smooth.t[1]
  get_smooth.t[1] = get_smooth.t[0]
  get_smooth.t[0] = x
  xs = (get_smooth.t[0]+get_smooth.t[1]+get_smooth.t[2])/3
  return(xs)


def update_screen(mode, show_letter = False):
  global temp_color
  if mode == "temp":
    if show_letter:
      show_t(temp_color)
    t1 = sense.get_temperature_from_humidity()
    t2 = sense.get_temperature_from_pressure()
    t_cpu = get_cpu_temp()
    h = sense.get_humidity()
    p = sense.get_pressure()

    # calculates the real temperature compesating CPU heating
    t = (t1+t2)/2
    t_corr = t - ((t_cpu-t)/1.5)
    t_corr = get_smooth(t_corr)
    #avg_sensor_temp = (sense.get_temperature() + sense.get_temperature_from_humidity() + sense.get_temperature_from_pressure()) / 3
    #amb_temp = 0.0071 * avg_sensor_temp* avg_sensor_temp + 0.86 * avg_sensor_temp - 10.0 - 3
    #amb_temp = sensor.get_temperature()
    #temp = sense.temp
    #temp_value = temp / 2.5 + 16
    #pixels = [red if i < temp_value else white for i in range(64)]
    color = l_blue
    if t_corr <= 20:
        color = l_blue
    elif ((t_corr > 20 ) and (t_corr <=35)):
        color = warning_color
    elif t_corr > 35:
        color = danger_color
    temp_color = color
    current_temp = math.trunc(t_corr)
    #print("t1=%.1f  t2=%.1f  t_cpu=%.1f  t_corr=%.1f  h=%d  p=%d" % (t1, t2, t_cpu, t_corr, round(h), round(p)))
    sense.set_pixels(display_digits(t_corr, color))

  elif mode == "pressure":
    if show_letter:
      show_p()
    pressure = sense.pressure
    pressure_value = pressure / 20
    sense.set_pixels(display_digits(pressure_value, green))
    #pixels = [green if i < pressure_value else white for i in range(64)]

  elif mode == "humidity":
    if show_letter:
      show_h()
    humidity_value = sense.humidity
    #humidity_value = 64 * humidity / 100
    sense.set_pixels(display_digits(humidity_value, blue))
    #pixels = [blue if i < humidity_value else white for i in range(64)]
  elif mode == "cpu":
    if show_letter:
      show_c()
    cpu_temp = get_cpu_temp()
    sense.set_pixels(display_digits(cpu_temp, (204, 0, 204)))

  elif mode == "ip":
    if show_letter:
      show_ip()
    ip = check_output(['hostname', '-I'])
    #ip = "b\192.168.8.101  \n"
    text = "%s"%ip
    #print(text[2:-3])
    sense.show_message(text[2:-3], text_colour=[153, 102, 51])

  elif mode == "reboot":
    if show_letter:
      show_r()
    sense.set_pixels(digit_Reboot((0, 255, 204)))

  elif mode == "clock":
    if show_letter:
      show_cl()
    hour = time.localtime().tm_hour
    minute = time.localtime().tm_min
    display_clock(hour, minute)
    #sense.set_pixels(digit_clock(red,blue))


####
# Intro Animation
####
show_cl()
show_t(red)
show_p()
show_h()
show_c()
show_ip()
show_r()




update_screen("clock")

index = 0
sensors = ["clock", "temp", "pressure", "humidity", "cpu", "ip", "reboot"]

####
# Main game loop
####

middle_held = False
middle_released = False
display_info = True

while True:
  selection = False
  events = sense.stick.get_events()
  test_var =  "test"
  for event in events:
    # Skip releases
    if display_info:
        if event.action != "released":
          if event.direction == "left":
            if index == 0:
                index = 6
            else:
                index -= 1
            selection = True
          elif event.direction == "right":
            if index == 6:
                index = 0
            else:
                index += 1
            selection = True
          if selection:
            current_mode = sensors[index % 7]
            update_screen(current_mode, show_letter = True)
            time.sleep(1)
        print("%s"%test_var)

    if event.action == "released":
        if event.direction == "middle":
          if middle_held:
              middle_released = True
          elif index == 6:
              #print("reboot")
              os.system('sudo shutdown -r now')


    if event.action == "held":
        if event.direction == "middle":
            middle_held = True



  if middle_held and middle_released:
      middle_held = False
      middle_released = False
      display_info = not display_info
      print ("Display: %r" % (display_info))

  if not selection:
      if display_info:
          current_mode = sensors[index % 7]
          update_screen(current_mode)
          time.sleep(1)
      else:
          sense.clear()
