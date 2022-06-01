PIPE="|"
ELBOW="└──"
TEE="├──"
PIPE_PREFIX="|  "
SPACE_PREFIX="   "

VALID_FORMATS = {
    "python": ["py", "pyx", "pyc"],
    "c": ["c", "h"],
    "js": ["js","jsx"],
    "json": ["json"],
    "html": ["html","htm"],
    "css": ["css","scss","sass"],
    "java": ["java"],
    "rust": ["rs"],
    "yaml": ["yaml","yml"],
    "xml": ["xml"],
    "bash": ["sh","bash"],
    "sql": ["sql"],
    "php": ["php"],
    "perl": ["pl","pm"],
    "ruby": ["rb"],
    "go": ["go"],
    "swift": ["swift"],
    "csharp": ["cs"],
    "typescript": ["ts"],
    "kotlin": ["kt"],
    "coffeescript": ["coffee"],
    "lua": ["lua"],
    "erlang": ["erl"],
    "haskell": ["hs"],
    "scala": ["scala"],
    "other": []
}

def load_valid_formats_list():
    avf = list(map(lambda k: k, VALID_FORMATS.values())) 
    AVF = [x for sl in avf for x in sl]
    return AVF


ALL_VALID_FORMATS = load_valid_formats_list()




VALID_FILE_FORMATS={
    "images": ["png","jpg","jpeg","gif","bmp","tiff","svg","ico"],
    "txt":["txt","doc","docx","odt","rtf","md"],
    "spreadsheets": ["xls","xlsx","ods","csv"],
    "pdf": ["pdf"],
    "audio": ["mp3","wav","flac","aiff","aac","ogg","wma","m4a","m4b","m4p","m4r","mp4","m4v","m4s","m4a","m4p","m4b","m4r","m4v","m4s","mp4","mp3","flac","aiff","aac","ogg","wma","m4a","m4b","m4p","m4r","m4v","m4s","mp4","mp3"],
    "video": ["mp4","m4v","m4s","m4a","m4p","m4b","m4r","m4v","m4s","mp4","mp3","flac","aiff","aac","ogg","wma","m4a","m4b","m4p","m4r","m4v","m4s","mp4","mp3"],
    "code": ["py","pyx","pyc","c","h","js","jsx","json","html","htm","css","scss","sass","java","rust","yaml","yml","sh","bash","sql","php","pl","pm","rb","go","swift","cs","ts","kt","coffee","lua","erl","hs","scala"],
    "other": []
    
}