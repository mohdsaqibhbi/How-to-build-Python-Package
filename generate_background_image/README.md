# Generate background image

This repo is about how to Generate a background image of words in a given string using the wordcloud module. A generated background image can be used in Git repos, blogs, or articles.

## Getting Started

### Installation

`pip3 install generate-background-image`

### Usage
- To generate image with black background.

```
generate_text_image -ws "Iron man,Thanos,Doctor Strange,Captain Marvel,Hulk,Vision,Thor,Groot,Rocket,Winter Soldier,Hela,Spiderman,Black Panther,Ultron,Wanda,Gamora,Star Lord,War Machine,Silver Quick,Mantis,Captain America,Loki,Antman,Black Widow,Hawkeye,Falcon,Drax,Shuri" -o output/mcu.png -l black
```
![mcu_black](https://github.com/mohdsaqibhbi/Generate_text_image/blob/master/output/mcu_black.png)

- To generate image with white background.

```
generate_text_image -ws "Iron man,Thanos,Doctor Strange,Captain Marvel,Hulk,Vision,Thor,Groot,Rocket,Winter Soldier,Hela,Spiderman,Black Panther,Ultron,Wanda,Gamora,Star Lord,War Machine,Silver Quick,Mantis,Captain America,Loki,Antman,Black Widow,Hawkeye,Falcon,Drax,Shuri" -o output/mcu_white.png -l white
```
![mcu_white](https://github.com/mohdsaqibhbi/Generate_text_image/blob/master/output/mcu_white.png)

### Command line arguments

| tag (* = required)| variable          | options                                        | default value   |
|:-----------------:|:------------------|:-----------------------------------------------|:----------------|
| -ws *             | word_string       | string of words separated by comma             | REQUIRED        |
| -o *              | out               | path to output image                           | "output_image.png"        |
| -l                | layout_color      | choices=["black", "white"]                     | "black"         |
| -W                | width             | width of image                                 | 1200            |
| -H                | height            | height of image                                | 800             |
| -s                | step_size         | difference between freqencies of words         | 50              |
| -b                | bias              | lowest initial frequency of a word             | 10              |

## LICENSE
This project is licensed under the terms of the [MIT license](LICENSE).

## Follow me

- Follow me on Linkedin: [mohdsaqibhbi](https://www.linkedin.com/in/mohdsaqibhbi)
- Subscribe my Youtube channel: [StarrAI](https://www.youtube.com/channel/UCooZBjTCrnM3LH1nIqAmDQA)