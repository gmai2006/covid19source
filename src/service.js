
getJson = async (url) => {
    const response = await fetch(url);
    const json = await response.json;
    window.localStorage.set(url, json);
}