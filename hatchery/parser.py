import os.path
from struct import Struct
from collections import namedtuple
from loguru import logger
import cstruct


class MachineStruct(cstruct.MemCStruct):
    __def__ = """
        #define MaxPacket 20

        struct MachineRecord {   
            unsigned int data01; // Неизвестно что это
            unsigned int TimeStamp; // Время записи
            //Данные зоны 1
            struct {
                short ZN1CV;
                short ZN1SetPoint;
                short ZN1data01; // 
                short ZN1LowAlarm;
                short ZN1HighAlarm;
                short ZN1data02; // 
                short ZN1data03; //
            } zone1;
            //Данные зоны 2
            struct {
                short ZN2CV;
                short ZN2SetPoint;
                short ZN2data01; // 
                short ZN2LowAlarm;
                short ZN2HighAlarm;
                short ZN2data02; // 
                short ZN2data03; //
            } zone2;
            //Данные зоны 3
            struct {
                short ZN3CV;
                short ZN3SetPoint;
                short ZN3data01; // 
                short ZN3LowAlarm;
                short ZN32ighAlarm;
                short ZN3data02; // 
                short ZN3data03; //
            } zone3;
            //Данные зоны 4
            struct {
                short ZN4CV;
                short ZN4SetPoint;
                short ZN4data01; // 
                short ZN4LowAlarm;
                short ZN4HighAlarm;
                short ZN4data02; // 
                short ZN4data03; // 
            } zone4;
            short unknownZones[14];
            //Humidity
            struct {
                short HumCV;
                short HumSetPoint;
                short Humdata01; // 
                short HumLowAlarm;
                short HumHighAlarm;
                short Humdata02; // 
                short Humdata03; //
            } humidity;
            //CO2
            struct {
                short CO2CV;
                short CO2SetPoint;
                short CO2LowAlarm;
                short CO2HighAlarm;
                short CO2data;
            } co2;
            //Damper
            struct {
                short DamperCV;
                short DamperSetPoint;
                short DamperMinValue;
            } damper;
            //AUXFan
            struct {
                short AUXFanMinDamperStart;
                short AUXFanData1;
                short AUXFanData2;
            } damper;
            short arrayD1[3]; // ХЗ что это 
            struct {
                short totalTimeDays;
                short totalTimeHors;
                short totalTimeMinutes;
            } timer;
            /// "Это ТАЙМЕР (!!!!!) Выполнения программы инкубационной"
            short arrayD2[4]; // Неизвестно что это
            short stageElapsedTime; // в десятых часа
            short a1;
            short a2;
            char CurrentStage;
            char isStartProgram;
            short a3;
            short a4;
            short TurnPosition;

            short arrayD3[9];
        };
    """


class SourceFileParser:
    def __init__(self):
        pass

    def parse_record(self, record):
        result = MachineStruct.unpack(record)
        return result

    def parse(self, file_path):
        try:
            with open(file_path, 'rb') as file:
                record = file.read(MachineStruct.size)
                data = self.parse_record(record)
        except Exception as ex:
            logger.error('Some issues while parsing')
