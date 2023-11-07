const url = 'https://github.com/jonh-nobre'
const url_2 = 'https://www.linkedin.com/in/jonh-nobre-172509241/' 
const url_3 = 'https://www.instagram.com/john_nobre38/'
const btn = document.querySelector('#myGitHub')
const btn_2 = document.querySelector('#myLinkedIn')
const btn_3 = document.querySelector('#myInstagram')

function openInNewTab(url) {
    window.open(url, '_blank')
}

btn.addEventListener('click', () => {
    openInNewTab(url)
})

btn_2.addEventListener('click', () => {
    openInNewTab(url_2)
})

btn_3.addEventListener('click', () => {
    openInNewTab(url_3)
})
