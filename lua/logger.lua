local request_body_size = tonumber(ngx.var.request_length)

if request_body_size then
    ngx.log(ngx.INFO, "Request body size: " .. request_body_size .. " bytes")
else
    ngx.log(ngx.WARN, "Unable to determine request body size")
end

local response_body_size = tonumber(ngx.var.bytes_sent)
if response_body_size then
    ngx.log(ngx.INFO, "Response body size: " .. response_body_size .. " bytes")
else
    ngx.log(ngx.WARN, "Unable to determine response body size")
end

local body_data, err = ngx.req.get_body_data()
if not body_data then
    ngx.log(ngx.WARN, "Error getting request body data: ", err)
    return
end

local filename = body_data:match('Content-Disposition:.-filename="([^"]*)"')
if filename then
    ngx.log(ngx.INFO, "Uploaded file name: " .. filename)
else
    ngx.log(ngx.WARN, "Unable to extract filename from request body")
end