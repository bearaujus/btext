import time
from threading import Thread
from IPython.display import clear_output

__author__ = 'Haryo Bagas Assyafah'
__copyright__ = 'Copyright 2020 Bear Au Jus - ジュースとくま'
__credits__ = ['Haryo Bagas Assyafah']
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Haryo Bagas Assyafah"
__email__ = "haryobagasasyafah6@gmail.com"
__status__ = "Production"

class ProcessViewer :
    def __init__(self, data_len, title = 'Processing') :
        if isinstance(data_len, list) :
            data_len = len(data_len)
        if not isinstance(data_len, int) :
            raise Exception('data_len must a valid integer')
        if data_len < 0 :
            raise Exception('failed to initiate process viewer. data_len cannot < 0')
            
        self.__title = title
        self.__data_len = data_len
        self.__idx = 0
        self.__stopper = False
                
    def start(self) :
        self.__process_show = Thread(target=self.__start_data_processing_view)
        self.__process_show.start()
        
    def set_index(self, idx) :
        self.__idx = idx + 1
        
    def set_title(self, title) :
        self.__title = title
        
    def stop(self) :
        time.sleep(0.1)
        self.__stopper = True
        self.__process_show.join()

    def __start_data_processing_view(self) :
        while True :
            self.__data_processing_view()
            time.sleep(0.001)
            if self.__stopper :
                break
        
    def __data_processing_view(self) :
        if self.__data_len == 0 :
            clear_output(wait=True)
            print(self.__get_text(1, 20, 20)) 
        else :
            progress = self.__idx / self.__data_len       
            bar_length = 20
            if progress < 0:
                progress = 0
            if progress >= 1:
                progress = 1
            block = int(round(bar_length * progress))

            clear_output(wait=True)
            print(self.__get_text(progress, block, bar_length))
                
    def __get_text(self, progress, block, bar_length) :
        if self.__data_len == 0 :
            return '{0}: [{1}] {2:.1f}% | P: {3} [ Done ]'.format(self.__title, '#' * block, 100, str(0) + ' / ' + str(0))
        elif self.__idx == self.__data_len :
            return '{0}: [{1}] {2:.1f}% | P: {3} [ Done ]'.format(self.__title, '#' * block + '-' * (bar_length - block), progress * 100, str(self.__idx) + ' / ' + str(self.__data_len))
        elif self.__idx <= 1 :
            return 'Preparing to {0} . . .'.format(self.__title)
        else :
            return '{0}: [{1}] {2:.1f}% | P: {3}'.format(self.__title, '#' * block + '-' * (bar_length - block), progress * 100, str(self.__idx) + ' / ' + str(self.__data_len))