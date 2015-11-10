const inputName = process.argv[2];
const inputMessage = process.argv[3];

// The WTF exercise.
function html(str, name, message) {
    const escaped = message
        .replace(/&/g, '&amp;')
        .replace(/'/g, '&apos;')
        .replace(/"/g, '&quot;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;');

    return str[0] + name + str[1] + escaped + str[2];
}

// No one will ever guess that format.
console.log(html`<b>${inputName} says</b>: "${inputMessage}"`);
