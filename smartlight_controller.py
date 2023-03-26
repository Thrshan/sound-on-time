import tuyacloud
import time
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

ACCESS_ID = os.environ.get("ACCESS_ID")
SECRET_KEY = os.environ.get("SECRET_KEY")
DEVICE_ID = os.environ.get("DEVICE_ID")
REGION_KEY = os.environ.get("REGION_KEY")
ENDPOINT_URL = os.environ.get("ENDPOINT_URL")

class Tuya_controller:
    def __init__(self) -> None:
        self.tcc = tuyacloud.TuyaCloudClientNicer(
            ACCESS_ID       = ACCESS_ID,
            ACCESS_SECRET   = SECRET_KEY,
            UID             = DEVICE_ID,
            ENDPOINT_URL    = ENDPOINT_URL
        )
    
    def exec_command(self, commands):
        exec_result = self.tcc.exec_device_command(DEVICE_ID, {"commands": commands})
        return exec_result
    
    def turn_on(self):
        cmd = [{
            "code": "switch_led",
            "value": True
        }]
        return self.exec_command(cmd)
    
    def turn_off(self):
        cmd = [{
            "code": "switch_led",
            "value": False
        }]
        return self.exec_command(cmd)
    
    def sweep_brightness(self):
        for i in range(100):
            cmd = [
              {
                "code": "bright_value_v2",
                "value": 10*i
              },
              {
                "code": "switch_led",
                "value": True
              }]
            res = self.exec_command(cmd)
            time.sleep(1)



'''
Code	Type	Values
switch_led	Boolean	
"{true,false}"
work_mode	Enum	
{
  "range": [
    "white",
    "colour",
    "scene",
    "music"
  ]
}
bright_value_v2	Integer	
{
  "min": 10,
  "max": 1000,
  "scale": 0,
  "step": 1
}
temp_value_v2	Integer	
{
  "min": 0,
  "max": 1000,
  "scale": 0,
  "step": 1
}
colour_data_v2	Json	
{
  "h": {
    "min": 0,
    "scale": 0,
    "unit": "",
    "max": 360,
    "step": 1
  },
  "s": {
    "min": 0,
    "scale": 0,
    "unit": "",
    "max": 1000,
    "step": 1
  },
  "v": {
    "min": 0,
    "scale": 0,
    "unit": "",
    "max": 1000,
    "step": 1
  }
}
scene_data_v2	Json	
{
  "scene_num": {
    "min": 1,
    "scale": 0,
    "max": 8,
    "step": 1
  },
  "scene_units": {
    "unit_change_mode": {
      "range": [
        "static",
        "jump",
        "gradient"
      ]
    },
    "unit_switch_duration": {
      "min": 0,
      "scale": 0,
      "max": 100,
      "step": 1
    },
    "unit_gradient_duration": {
      "min": 0,
      "scale": 0,
      "max": 100,
      "step": 1
    },
    "bright": {
      "min": 0,
      "scale": 0,
      "max": 1000,
      "step": 1
    },
    "temperature": {
      "min": 0,
      "scale": 0,
      "max": 1000,
      "step": 1
    },
    "h": {
      "min": 0,
      "scale": 0,
      "unit": "",
      "max": 360,
      "step": 1
    },
    "s": {
      "min": 0,
      "scale": 0,
      "unit": "",
      "max": 1000,
      "step": 1
    },
    "v": {
      "min": 0,
      "scale": 0,
      "unit": "",
      "max": 1000,
      "step": 1
    }
  }
}
countdown_1	Integer	
{
  "min": 0,
  "max": 86400,
  "scale": 0,
  "step": 1
}
music_data	Json	
{
  "change_mode": {
    "range": [
      "direct",
      "gradient"
    ]
  },
  "bright": {
    "min": 0,
    "scale": 0,
    "unit": "",
    "max": 1000,
    "step": 1
  },
  "temperature": {
    "min": 0,
    "scale": 0,
    "unit": "",
    "max": 1000,
    "step": 1
  },
  "h": {
    "min": 0,
    "scale": 0,
    "unit": "",
    "max": 360,
    "step": 1
  },
  "s": {
    "min": 0,
    "scale": 0,
    "unit": "",
    "max": 255,
    "step": 1
  },
  "v": {
    "min": 0,
    "scale": 0,
    "unit": "",
    "max": 255,
    "step": 1
  }
}
control_data	Json	
{
  "change_mode": {
    "range": [
      "direct",
      "gradient"
    ]
  },
  "bright": {
    "min": 0,
    "scale": 0,
    "unit": "",
    "max": 1000,
    "step": 1
  },
  "temperature": {
    "min": 0,
    "scale": 0,
    "unit": "",
    "max": 1000,
    "step": 1
  },
  "h": {
    "min": 0,
    "scale": 0,
    "unit": "",
    "max": 360,
    "step": 1
  },
  "s": {
    "min": 0,
    "scale": 0,
    "unit": "",
    "max": 255,
    "step": 1
  },
  "v": {
    "min": 0,
    "scale": 0,
    "unit": "",
    "max": 255,
    "step": 1
  }
}
rhythm_mode	Raw	
{
  "maxlen": 255
}
sleep_mode	Raw	
{
  "maxlen": 255
}
wakeup_mode	Raw	
{
  "maxlen": 255
}
power_memory	Raw	
{}
do_not_disturb	Boolean	
"{true,false}"
'''