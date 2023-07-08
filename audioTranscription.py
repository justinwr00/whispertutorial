import whisper
import re


#file to remove whitespace and fix punctuation
fileName = "a1.mp3"


model = whisper.load_model('base')
result = model.transcribe(fileName, fp16=False)

transcript = result['text']
#print(transcript)

def format_punctuation(text):
    # Add a single space after commas, periods, question marks, and exclamation marks
    formatted_text = re.sub(r'([,.\?!])(?!\s)', r'\1 ', text)
    return formatted_text


def space_reduce(text):
    # Reduce multiple spaces after commas, periods, question marks, and exclamation marks to a single space
    formatted_text = re.sub(r'([,.\?!])\s+', r'\1 ', text)
    return formatted_text

def reduce_extra_spaces(text):
    # Reduce multiple spaces between words to a single space
    formatted_text = re.sub(r'(\b\w+)\s{2,}(\b\w+)', r'\1 \2', text)
    return formatted_text

transcript = format_punctuation(transcript)
transcript = space_reduce(transcript)
transcript = reduce_extra_spaces(transcript)

#save updated file
updatedFile = open(fileName + '_transcribed.txt', 'w', encoding='utf8')
updatedFile.write(transcript)
updatedFile.close()