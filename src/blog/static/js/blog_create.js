const topicInput =  document.querySelector("input[name=topic]");
const slugInput = document.querySelector("input[name=slug]");
const slugify = (val) => {
    return val.toString().trim()
    .replace(/&/g, '-and-') // replace & with '-and-'
    .replace(/[\s\W-]+/g, '-')

};
topicInput.addEventListener("keyup", (e) => {
        slugInput.setAttribute('value', slugify(topicInput.value));

});

