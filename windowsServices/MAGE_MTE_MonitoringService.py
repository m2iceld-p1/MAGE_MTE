import servicemanager
import socket
import sys
import win32event
import win32service
import win32serviceutil

class MAGE_MTE_MonitoringService(win32serviceutil.ServiceFramework):
    _svc_name_ = "MAGE_MTE_MonitoringService" #Service Name (exe)
    _svc_display_name_ = "MAGE_MTE_MonitoringService" #Service Name which will display in the Winfows Services Window 
    _svc_description_ = "" ##Service Name which will display in the Winfows Services Window

    def __init__(self, args):
        '''
        Used to initialize the service utility. 
        '''
        print("init")
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60000)

    def SvcStop(self):
        '''
        Used to stop the service utility (restart / timeout / shutdown)
        '''
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        '''
        Used to execute all the piece of code that you want service to perform.
        '''
        print("has started")
        rc = None
        while rc != win32event.WAIT_OBJECT_0:
            with open('C:\\MAGE_MTE_MonitoringService.log', 'a') as f:
                f.write('MAGE_MTE_MonitoringService running...\n')
            rc = win32event.WaitForSingleObject(self.hWaitStop, 10)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(MAGE_MTE_MonitoringService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(MAGE_MTE_MonitoringService)