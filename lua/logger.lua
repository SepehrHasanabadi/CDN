local request_url = ngx.var.request_uri
local request_method = ngx.req.get_method()
if request_url == "/v1/cache-file" and request_method == "POST" then
  local file, err = io.open("/usr/local/openresty/nginx/logs/minification.log", "a")
  if not file then
      return false, err
  end
  local log = ""
  local request_body_size = tonumber(ngx.var.request_length)
  if request_body_size then
    log = log .. "Request body size: " .. request_body_size .. " bytes\n"
  else
    log = log .. "Unable to determine request body size\n"
  end
  
  local response_size = tonumber(ngx.var.bytes_sent) or 0
  log = log .. "Response Size: " .. response_size .. " bytes\n\n"
  
  file:write(log)
  file:flush()
  file:close()
end
