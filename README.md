<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/AlexisLib/NLP-VibeCatcher">
    <img src="image/VibeCatcher.png" alt="Logo">
  </a>

  <h3 align="center">VibeCatcher</h3>

  <p align="center">
    The aim of the Vibe Catcher project is to learn about the dominant sentiment evoked by a hashtag. From a user perspective, this will allow entering a hashtag in a search box and retrieving the general sentiment it evokes on social media Twitter and Instagram. The general sentiment will be returned under negative, neutral and positive percentage.
    <br />
    <br />
    <a href="https://github.com/AlexisLib/NLP-VibeCatcher">View Demo</a>
    ·
    <a href="https://github.com/AlexisLib/NLP-VibeCatcher/issues">Report Bug</a>
    ·
    <a href="https://github.com/AlexisLib/NLP-VibeCatcher/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<p align="center">
  <a href="https://github.com/AlexisLib/NLP-VibeCatcher">
    <img src="image/covid.JPG">
  </a>
 </p>


The aim of the Vibe Catcher project is to learn about the dominant sentiment evoked by a hashtag. From a user perspective, this will allow entering a hashtag in a search box and retrieving the general sentiment it evokes on social media Twitter and Instagram. The general sentiment will be returned under negative, neutral and positive percentage.

From a more technical point of view, it will therefore be necessary to retrieve the user's request first, then retrieve all the posts / tweets containing it from APIs (or other means of retrieval) of social networks. Then these posts will be analyzed using machine learning, sentiment classification, and the percentages returned to the user, these percentages represent the general appreciation of people who spoke by mentioning this hashtag.


### Built With

* [Python](https://www.python.org/)


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

You need to get Python for run this project.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/AlexisLib/NLP-VibeCatcher.git
   ```
   
 2. Install core spacy
     ```sh
    python -m spacy download en_core_news_sm
    python -m spacy download fr_core_news_sm
     ```
     
 3. Run main.py
   

<!-- USAGE EXAMPLES -->
## Usage

<p align="center">
  <a href="https://github.com/AlexisLib/NLP-VibeCatcher">
    <img src="image/result.JPG" alt="Logo">
  </a>
</p>

- First step : you can choose a network, twitter or instagram.
- Second Step : you can choose the hashtag you want to analyse.
- Third step : you can choose the number of tweet / post you want for the analyse.
- Final step : you can choose the language between english (en) or french (fr).


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/AlexisLib/NLP-VibeCatcher/issues) for a list of proposed features (and known issues).


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- CONTACT -->
## Contact

Project Link: [https://github.com/AlexisLib/NLP-VibeCatcher](https://github.com/AlexisLib/NLP-VibeCatcher)




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/AlexisLib/NLP-VibeCatcher.svg?style=for-the-badge
[contributors-url]: https://github.com/AlexisLib/NLP-VibeCatcher/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/AlexisLib/NLP-VibeCatcher.svg?style=for-the-badge
[forks-url]: https://github.com/AlexisLib/NLP-VibeCatcher/network/members
[stars-shield]: https://img.shields.io/github/stars/AlexisLib/NLP-VibeCatcher.svg?style=for-the-badge
[stars-url]: https://github.com/AlexisLib/NLP-VibeCatcher/stargazers
[issues-shield]: https://img.shields.io/github/issues/AlexisLib/NLP-VibeCatcher.svg?style=for-the-badge
[issues-url]: https://github.com/AlexisLib/NLP-VibeCatcher/issues
[license-shield]: https://img.shields.io/github/license/AlexisLib/NLP-VibeCatcher.svg?style=for-the-badge
[license-url]: https://github.com/AlexisLib/NLP-VibeCatcher/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/alexis-l-45864611a/
