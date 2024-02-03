# FastAPI File Storage and Minification Service

## Overview

This FastAPI application provides a file storage and minification service where users can store files with an option to minify them. The application includes user signup, token retrieval, and file storage functionalities.

## Postman Collection

The Postman collection can be found in the `postman` directory. It's recommended to use the Postman environment to set variables like `base_url` in the requests.

## Endpoints

### Health Check

- **Endpoint:** `/health`
- **Description:** Check the NGINX status to ensure the service is alive.

### User Signup

- **Endpoint:** `/v1/sign-up`
- **Description:** Create a new user. The username should not be taken before.

### Token Retrieval

- **Endpoint:** `/v1/token`
- **Description:** Retrieve a token to perform the file requests.

### File Storage

#### Store a File (POST)

- **Endpoint:** `/v1/cache-file`
- **Description:** Store a file. The user can specify the `minify` parameter in the form request as `true` if the file needs to be minified.

  **Response:**
  ```json
  {
    "size": "101.88 KB",
    "minify_duration": "0.000000 ms",
    "minify_ram_consumption": "0.00 B",
    "type": ".png",
    "created_at": "2024-02-02T09:29:06.135570Z"
  }
- all the files will be stored in the `upload_base_file` path which is defined in the `.env` file
- the supported formats for the minification are: 
```
css,
js,
jpeg,
png,
gif,
bmp,
tiff,
svg,
ico
```
- all the image formats will be minfied by WEBP.
- the `minify_duration` and `minify_ram_consumption` fields are zero if the `minify` is false and it stores the original file.

#### Retrieve Files (GET)

- **Endpoint:** `/v1/cache-file`
- **Description:** Get all the user files.

## Lua Logs
the minification logs are storing in `./nginx/logs/minification.log`

## Test
run the `pytest` command in the container. the container terminal can be access by running the `docker exec -it <container-id> sh` for its app container.