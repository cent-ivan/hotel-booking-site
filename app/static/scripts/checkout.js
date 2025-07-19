//define the elements
const totalPriceEle = document.getElementById('total-price') //DISPLAY
const roomNameEle = document.querySelectorAll('#room-name')
const roomPriceEle = document.querySelectorAll('#room-price') //room's price
const totalNights = document.getElementById('total-nights')

const numberInput = document.querySelectorAll('#qty') //number input

//price incrementer
let totalPrice = 0
let rooms = {}

//computes prices
const displayPrice = () => {
    totalPriceEle.value = totalPrice.toLocaleString('en-US', {
                            style: 'currency',
                            currency: 'PHP'
                        });
}

//adding event listner
let count = 0
numberInput.forEach(numInput => {
    const roomName = roomNameEle[count].outerText
    const roomPrice = roomPriceEle[count].value

    //initial price display
    rooms[roomName] = {price:roomPrice}
    console.log(rooms)
    totalPrice=0
    for (key in rooms) {
        totalPrice += (parseFloat(rooms[key].price) * parseInt(totalNights.innerText))
    }
    displayPrice()
    numInput.addEventListener('input', () => {
        const price = ((roomPrice * parseInt(totalNights.innerText)) * numInput.value)
        rooms[roomName] = {price:price}
        totalPrice = 0
        for (key in rooms) {
            totalPrice += (parseFloat(rooms[key].price))
        }
        displayPrice()
    })
    count += 1
})


//-Model Notice------------
const childrenModal = document.getElementById('note-surcharge')
const showModal = document.getElementById('show-surcharge')

childrenModal.addEventListener('click', ()=> {
    childrenModal.classList.add('hidden')
})

showModal.addEventListener('click', ()=> {
    childrenModal.classList.remove('hidden')
})
