# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    servo.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tvilella <vilelladev@outlook.com>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/01/22 10:33:31 by tvilella          #+#    #+#              #
#    Updated: 2023/01/22 10:45:57 by tvilella         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from machine import Pin, PWM

# ================ Classe Servo ================
class Servo:
    # Definições de constantes no escopo da classe evitando colisão
    __PULSE_MIN = 1768
    __PULSE_MAX = 7802
    __PULSE_90G = 4876
    __FREQ = 50

    # Construtor
    def __init__(self):
        self._freq = Servo.__FREQ           # T ~ 20000 us
        self._pulse_min = Servo.__PULSE_MIN # 0º ~ 544 us
        self._pulse_max = Servo.__PULSE_MAX # 180º ~ 2400 us
        self._duty = Servo.__PULSE_90G      # 90º ~ 1500 us         

    # Configura o pino e inicia o PWM a 90º
    def attach(self, pino):
        self.pin = Pin(pino)
        self.pwm = PWM(self.pin)
        self.pwm.freq(self.freq)
        self.pwm.duty_u16(self.duty)
       
    # Recebe o angulo e controla o servo
    def write(self, angulo):
        self.duty = self._convert(angulo)
        self.pwm.duty_u16(self.duty)
    
    # Converte o angulo em pulso
    def _convert(self, angulo):
        if (not(isinstance(angulo, int))):
            raise ValueError(f"Valor {angulo} inválido")
        
        if angulo <= 0:
            return self.pulse_min
        if (Servo.__PULSE_MIN <= angulo <= Servo.__PULSE_MAX):
            return angulo
        elif angulo >= 180:
            return self.pulse_max
        
        pulso = self.pulse_min + int( (angulo / 180) * (self.pulse_max - self.pulse_min) )
        return pulso
    
    # Getter e Setter de _freq
    @property
    def freq(self):
        return self._freq
    @freq.setter
    def freq(self, x):
        if (not(isinstance(x, int) and x > 0)):
            raise ValueError(f"Valor de {x} inválido!")
        self._freq = x

    # Getter e Setter de _pulse_min
    @property
    def pulse_min(self):
        return self._pulse_min
    @pulse_min.setter
    def pulse_min(self, x):
        if (not(isinstance(x, int) and x > 0) ):
            raise ValueError(f"Valor {x} inválido!")
        self._pulse_min = x
    
    # Getter e Setter de _pulse_max
    @property
    def pulse_max(self):
        return self._pulse_max
    @pulse_max.setter
    def pulse_max(self, x):
        if (not(isinstance(x, int) and x > 0) ):
            raise ValueError(f"Valor {x} inválido!")
        self._pulse_max = x
    
    # Getter e Setter de _duty
    @property
    def duty(self):
        return self._duty
    @duty.setter
    def duty(self, x):
        if (not(isinstance(x, int) and x > 0) ):
            raise ValueError(f"Valor {x} inválido!")
        if (x >= 65025):
            raise ValueError(f"Valor {x} maior que 16bits")
        self._duty = x

# ============== Fim Classe Servo ==============


# ==== Basic Test ====
    #todo
# ==== Basic Test ====