local cjson = require("cjson")

local function check_health()
    return true
end

local response = {
    status = check_health()
}
local json_response = cjson.encode(response)
ngx.header.content_type = "application/json"
ngx.say(json_response)