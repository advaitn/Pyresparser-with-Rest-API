
# Pyresparser with REST API support

This is an exteneded version of https://github.com/OmkarPathak/pyresparser, the main purpose of this repo is to provide a REST API end-point to the code. This repo uses Python Flask to achieve results.




## API Reference

#### Parse a Resume

```http
  POST /parse
```
To be passed in body as form-data

| Key | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `file` | `file` | **Required**. Absolute path to your file |


## Usage/Examples

```curl
curl --location --request POST 'localhost:5000/parse' \
--form 'file=@"/C:/Users/Desktop/resume.pdf"'
}
```

```json
{
    "data":  {
    'college_name': ['Marathwada Mitra Mandal’s College of Engineering'],
    'company_names': None,
    'degree': ['B.E. IN COMPUTER ENGINEERING'],
    'designation': ['Manager',
                    'TECHNICAL CONTENT WRITER',
                    'DATA ENGINEER'],
    'email': 'omkarpathak27@gmail.com',
    'mobile_number': '8087996634',
    'name': 'Omkar Pathak',
    'no_of_pages': 3,
    'skills': ['Operating systems',
              'Linux',
              'Github',
              'Testing',
              'Content',
              'Automation',
              'Python',
              'Css',
              'Website',
              'Django',
              'Opencv',
              'Programming',
              'C',
              ...],
    'total_experience': 1.83
  },
    "message": "File successfully uploaded"
}
```


## Installation

Create folder uploads in your installation directory
```bash
  mkdir uploads
```
Install dependencies
```bash
  pip install -r requirements.txt
```
Run main file
```bash
  python main.py
```
    

## Related

A simple resume parser used for extracting information from resumes [OmkarPathak/pyresparser](https://github.com/OmkarPathak/pyresparser)

