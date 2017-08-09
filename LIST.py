# define the registers:
# Manufacturer: ST electronics
# MPN: LIS3DH
# Description: 3 axis acceleromter

#import SMBUS for I2C read/write functions
from smbus import SMBus

#Register address map
# add this comment here for a git fetch test

STATUS_REG_AUX = 0x07
OUT_ADC1_L = 0x08
OUT_ADC1_H = 0x09
OUT_ADC2_L = 0x0A 
OUT_ADC2_H = 0x0B
OUT_ADC3_L = 0x0C
OUT_ADC3_H = 0x0D
# 0x0E - Reserved
WHO_AM_I = 0x0F
# 0x10 - 0x1D - Reserved
CTRL_REG0 = 0x1E
TEMP_CFG_REG = 0x1F
CTRL_REG1 = 0x20
CTRL_REG2 = 0x21
CTRL_REG3 = 0x22
CTRL_REG4 = 0x23
CTRL_REG5 = 0x24
CTRL_REG6 = 0x25
REFERENCE = 0x26
STATUS_REG = 0x27
OUT_X_L = 0x28
OUT_X_H = 0x29
OUT_Y_L = 0x2A
OUT_Y_H = 0x2B
OUT_Z_L = 0x2C
OUT_Z_H = 0x2D
FIFO_CTRL_REG = 0x2E 
FIFO_SRC_REG = 0x2F
INT1_CFG = 0x30
INT1_SRC = 0x31
INT1_THS = 0x32
INT1_DURATION = 0x33 
INT2_CFG = 0x34
INT2_SRC = 0x35
INT2_THS = 0x36
INT2_DURATION = 0x37 
CLICK_CFG = 0x38
CLICK_SRC = 0x39
CLICK_THS = 0x3A
TIME_LIMIT = 0x3B
TIME_LATENCY = 0x3C
TIME_WINDOW = 0x3D
ACT_THS = 0x3E
ACT_DUR = 0x3F


bus = SMBus(1)

# function to read acceleration registers: 
def z_output():
	z_output_L = bus.read_byte_data(0x18, OUT_Z_L)
	z_output_H = bus.read_byte_data(0x18, OUT_Z_H)
	z_output = (z_output_H << 8) | z_output_L
	print(z_output)
	print(z_output_L)
	print(z_output_H)


	
