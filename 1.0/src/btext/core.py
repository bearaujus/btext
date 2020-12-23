import re
import string
from btext.utill import ProcessViewer as pv

__author__ = 'Haryo Bagas Assyafah'
__copyright__ = 'Copyright 2020 Bear Au Jus - ジュースとくま'
__credits__ = ['Haryo Bagas Assyafah']
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Haryo Bagas Assyafah"
__email__ = "haryobagasasyafah6@gmail.com"
__status__ = "Production"

def conslet(val, sep = ' ') :
    '''
    Converting Text to Consecutive Letter
    '''
    return sep.join(i for i in re.findall('[a-zA-Z]+', val))
        
def conslet_tokenized(val, sep = ' ') :
    '''
    Converting Text to Tokenized Consecutive Letter
    '''
    val = [conslet(i) for i in val.split(sep)]
    return [i for i in val if i != '']

def consnum(val, sep = '') :
    '''
    Converting Text to Consecutive Number
    '''
    return sep.join(i for i in re.findall('[0-9]+', val))

def consnum_tokenized(val) :
    '''
    Converting Text to Tokenized Consecutive Number
    '''
    return re.findall('[0-9]+', val)
        
def conspunc(val, sep = '') :
    '''
    Converting Text to Consecutive Punctuation
    '''
    return sep.join(i for i in val if i in getall_punc_tokenized())
        
def conspunc_tokenized(val) :
    '''
    Converting Text to Tokenized Consecutive Punctuation
    '''
    return [i for i in val if i in conspunc(val)]

def lower(val) :
    '''
    Converting Text to Lower Case
    '''
    return val.lower()
        
def remove_spaces(val) :
    '''
    Removing Spaces 
    '''
    return re.sub(' ', '', val)
        
def remove_double_spaces(val) :
    '''
    Removing Double Spaces
    '''
    return re.sub(' +', ' ', val)
        
def removeby_char(val, exclude, sep = '') :
    '''
    Removing Char by User Option
    '''
    if isinstance(exclude, str) :
        return remove_double_spaces(re.sub(exclude, sep, val)).lstrip()
                        
    elif isinstance(exclude, list) :
        for i in exclude :
            val = remove_double_spaces(re.sub(i, sep, val)).lstrip()
        return val
    else :
        raise Exception('exclude must a valid string or list')
        
def removeby_length(val, exclude, sep = ' ') :
    '''
    Removing Char by User Desired Length
    '''
    output = []
    if isinstance(exclude, int) :
        for i in val.split(' ') :
            if len(i) != exclude :
                output.append(i)
                        
    elif isinstance(exclude, list) :
        for i in val.split(' ') :
            if len(i) not in exclude :
                output.append(i)
    else :
        raise Exception('exclude must a valid string or int')
            
    return sep.join(i for i in output)
        
def getall_alphabet(sep = '', include_upper = False) :
    '''
    Get All Valid Alphabet
    '''
    output = ''
    if include_upper :
        output = string.ascii_lowercase + string.ascii_uppercase
    else :
        output = string.ascii_lowercase
    return sep.join(i for i in output)
        
def getall_alphabet_tokenized(include_upper = False) :
    '''
    Get Tokenized All Valid Alphabet
    '''
    return [i for i in getall_alphabet(include_upper = include_upper)]
        
def getall_number(sep = '') :
    '''
    Get All Valid Number
    '''
    return sep.join(i for i in '0123456789')
        
def getall_number_tokenized() :
    '''
    Get Tokenized All Valid Number
    '''
    return [i for i in getall_number()]
        
def getall_punc(sep = '') :
    '''
    Get All Valid Punctuation
    '''
    return sep.join(i for i in string.punctuation)
        
def getall_punc_tokenized() :
    '''
    Get Tokenized All Valid Punctuation
    '''
    return [i for i in getall_punc()]

def normalize(obj, show_process = False) :
    '''
    Normalizing a Text or a Collections
    
    + Converting Text to Consecutive Letter
    + Converting Text to Lower Case
    + Removing Double Spaces
    '''
    def proc(obj) :
        obj = conslet(obj)
        obj = lower(obj)
        obj = remove_double_spaces(obj)
        return obj
    
    if isinstance(obj, int) :
        raise Exception('object must a valid collections or string')
    elif isinstance(obj, str) :
        return proc(obj)
    elif not all(isinstance(item, str) for item in obj) :
        raise Exception('all collections element must a valid string')
            
    output_obj = []
    append = output_obj.append
    if show_process :
        p = pv(len(obj), 'Normalizing Data')
        set_index = p.set_index
        p.start()
        for i, item in enumerate(list(obj)) :
            item = proc(item)
            append(item)
            set_index(i)
        p.stop()
    else :
        for i, item in enumerate(list(obj)) :
            item = proc(item)
            append(item) 
    return output_obj

def to_string(obj) :
    '''
    Converting Object to String
    '''
    if isinstance(obj, int) :
        return str(obj)
    elif isinstance(obj, float) :
        return str(obj)
    elif isinstance(obj, str) :
        return obj
    return ' '.join(str(i) for i in obj)