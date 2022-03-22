import random
import argparse
import wordcloud
from wordcloud import WordCloud

def generate_background_image(words, out="output_image.png", layout_color="black", width=1200, height=800, step_size=50, bias=10):

    '''
    Generate an image of words in a given string using wordcloud module.

    Argument:
        words -- string of words separated by comma
        out -- path to output image
        layout_color -- background color
        width -- width of image
        height -- height of image
        step_size -- difference between freqencies of words
        bias -- lowest initial frequency of a word

    Returns:
        None
    '''

    word_list = words.split(',')[::-1]

    text_list = []
    for i, word in enumerate(word_list):
        for j in range(i*step_size+bias):
            text_list.append(word)
    random.shuffle(text_list)
    text_corpus = " ".join(text_list)

    image = WordCloud(background_color=layout_color, height=height, width=width).generate(text_corpus)
    image.to_file(out)
    print("Image successfully saved to {}".format(out))