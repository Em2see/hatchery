import os.path
from struct import Struct
from collections import namedtuple
from loguru import logger


data_struct = Struct(7 * 'h')
humidity_struct = Struct(7 * 'h')
co2_struct = Struct(5 * 'h')
damper_struct = Struct('hhh')
aux_fan_struct = Struct('hhh')
unknown3 = Struct('hhh')
unknown4 = Struct('hhh')
total_struct = Struct('hhh')


machine_struct = {
    'data01': Struct('I'),
    'timeStamp': Struct('I'),
    'zone1': data_struct,
    'zone2': data_struct,
    'zone3': data_struct,
    'zone4': data_struct,
    'unknown7': data_struct,
    'humidity': humidity_struct,
    'co2': co2_struct,
    'damper': damper_struct,
    'aux_fan': aux_fan_struct,
    'unknown3': Struct('hhh'),
    'total': total_struct,
    'unknown4': Struct('hhhh'),
    'stageElapsedTime': Struct('h'),
    'a1': Struct('h'),
    'a2': Struct('h'),
    'CurrentStage': Struct('c'),
    'isStartProgram': Struct('c'),
    'a3': Struct('h'),
    'a4': Struct('h'),
    'TurnPosition': Struct('h'),
    'tail': Struct(9 * 'h')
}


MachineRecord = namedtuple('MachineRecord', ' '.join(machine_struct))
MachineStruct = Struct(''.join(v.format for v in machine_struct.values()))


class SourceFileParser:
    def __init__(self):
        pass

    def parse_record(self, record):
        result = MachineRecord._make(MachineStruct.unpack(record))
        return result

    def parse(self, file_path):
        try:
            with open(file_path, 'rb') as file:
                record = file.read(MachineStruct.size)
                data = self.parse_record(record)
        except Exception as ex:
            logger.error('Some issues while parsing')
