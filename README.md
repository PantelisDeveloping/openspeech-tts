<!-- Improved compatibility of back to top-->
<a id="readme-top"></a>
![Contributors][contributors-shield]
![Forks][forks-shield]
![Stargazers][stars-shield]
![Issues][issues-shield]
![MIT License][license-shield]
![LinkedIn][linkedin-shield]



<!-- PROJECT LOGO -->
<br />
<div align="left">
    
  <h3 align="center">OpenSpeech TTS API</h3>

  <p align="center">
    A simple and effective Text-to-Speech API compatible with OpenAI's endpoint
    <br />
    <a href="https://github.com/PantelisDeveloping"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/PantelisDeveloping">View Demo</a>
    ·
    <a href="https://github.com/PantelisDeveloping">Report Bug</a>
    ·
    <a href="https://github.com/PantelisDeveloping>Request Feature</a>
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

OpenSpeech TTS is a user-friendly and efficient Text-to-Speech (TTS) API designed to seamlessly integrate with OpenAI's powerful text-to-speech capabilities. This project aims to provide developers with a simple and effective tool to convert text into natural-sounding speech, making it ideal for various applications such as voice assistants, audiobooks, and accessibility tools.

Key Features:

Compatibility with OpenAI's API: Leverages OpenAI's advanced text-to-speech models to deliver high-quality audio output.
Ease of Use: Provides a straightforward interface for developers to integrate TTS functionality into their projects.
Efficiency: Optimized for performance to ensure smooth and responsive TTS generation. No need for GPU.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

We used Python + Flask + Gevent WSGI for depolyment and Edge TTS for the TTS support.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Edge](https://img.shields.io/badge/Edge-0078D7?style=for-the-badge&logo=Microsoft-edge&logoColor=white)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is how you will succesfully run your OpenSpeech TTS Server:

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
Python 3.10 + above with the following libarires in a virtual environment:
  ```sh
  pip install Flask
  pip install edge-tts
  pip install cryptography
  pip install gevent
  pip install art
  
  ```

### Installation

_Below is a step by step installation guide to run succesfuly the TTS Server._

1. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
3. Create & Activate a Virtual Environment in Python
   ```sh
   python -m venv /path/to/new/virtual/environment
   source <venv>/bin/activate
   ```
4. Run the api.py python
   ```js
   cd ./openspeech-tts/main
   python api.py
   ```
5. When prompted, enter the desired API key that you want to access the server & the Port to forward the API
   ```sh
   Enter API Key: ....
   Enter Port: ....
   ```
6. The server is up and ready to run!

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

You can use the TTS API in the same way you use the OpenAI Text-to-Speech:
```sh
    curl http://localhost:5000/v1/audio/speech \
      -H "Authorization: Bearer API-KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "tts-1",
        "input": "Today is a wonderful day to build something people love!",
        "voice": "alloy"
      }' \
      --output speech.mp3
   ```

_For the request example, please refer to the [Sample Request Curl](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add Changelog
- [x] Add main api.py file
- [ ] Add Additional Examples
- [ ] Adding secure https connection
- [ ] Adding more endpoints from OpenAI API
    - [ ] v1/audio/translations
    - [ ] v1/audio/transcriptions

See the [open issues](https://github.com/PantelisDeveloping/openspeech-tts/) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b PantelisDeveloping/openspeech-tts`)
3. Commit your Changes (`git commit -m 'Committing changes'`)
4. Push to the Branch (`git push origin PantelisDeveloping/openspeech-tts`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Pantelis - pantelis.developing@gmail.com

Project Link: [https://github.com/PantelisDeveloping/openspeech-tts](https://github.com/PantelisDeveloping/openspeech-tts)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
