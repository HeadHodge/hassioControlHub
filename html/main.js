import hass from "http://192.168.0.164/index.js"
 
async function main () {
  // Assuming hass running in `localhost`, under the default `8321` port:
  const client = await hass({
    token: 'my-secret-token'
  })
}   