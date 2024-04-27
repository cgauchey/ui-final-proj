// enable draggables to be dropped into this
interact('.dropzone').dropzone({
    // only accept elements matching this CSS selector
    accept: '.yes-drop',
    // Require a 75% element overlap for a drop to be possible
    overlap: 0.75,

    // listen for drop related events:

    ondropactivate: function (event) {
        // add active dropzone feedback
        event.target.classList.add('drop-active')
    },
    ondragenter: function (event) {
        var draggableElement = event.relatedTarget
        var dropzoneElement = event.target
        // feedback the possibility of a drop
        dropzoneElement.classList.add('drop-target')
        draggableElement.classList.add('can-drop')
        //draggableElement.textContent = 'Dragged in'
    },
    ondragleave: function (event) {
        var draggableElement = event.relatedTarget
        var dropzoneElement = event.target
        dropzoneElement.classList.add('drop-target')
        draggableElement.classList.remove('can-drop')

        //event.relatedTarget.textContent = 'Dragged out'
    },
    ondrop: function (event) {
        var draggableElement = event.relatedTarget
        var dropzoneElement = event.target
        dropzoneElement.append(draggableElement);
        //draggableElement.style.webkitTransform = draggableElement.style.transform = "translate(0px, 0px)";
        // update the posiion attributes
        draggableElement.setAttribute('data-x', 0)
        draggableElement.setAttribute('data-y', 0)
        //if (!draggableElement.classList.contains('text-overflow-ellipsis')) {
        //    draggableElement.classList.add('text-overflow-ellipsis')
        //}
        draggableElement.setAttribute('data-dropped-into', dropzoneElement.id);

    },
    ondropdeactivate: function (event) {
        var draggableElement = event.relatedTarget
        if (!draggableElement.classList.contains("can-drop")) {
            draggableElement.style.webkitTransform = draggableElement.style.transform = "translate(0px, 0px)";
            // update the posiion attributes
            draggableElement.setAttribute('data-x', 0)
            draggableElement.setAttribute('data-y', 0)
        }
        // remove the drop feedback style
        event.target.classList.remove('drop-target')
        event.relatedTarget.classList.remove('can-drop')
        // remove active dropzone feedback
        event.target.classList.remove('drop-active')
        event.target.classList.remove('drop-target')
    }
})

interact('.drag-drop')
    .draggable({
        inertia: true,
        modifiers: [
            interact.modifiers.restrictRect({
                restriction: '#listOfExpectation',
                endOnly: true,
                //elementRect: { top: 0, left: 0, bottom: 1, right: 1 }
            })
        ],
        autoScroll: true,
        // dragMoveListener from the dragging demo above
        onmove: dragMoveListener
    })




function dragMoveListener(event) {
    var target = event.target
    // keep the dragged position in the data-x/data-y attributes
    var x = (parseFloat(target.getAttribute('data-x')) || 0) + event.dx
    var y = (parseFloat(target.getAttribute('data-y')) || 0) + event.dy

    // translate the element
    target.style.webkitTransform =
        target.style.transform =
        'translate(' + x + 'px, ' + y + 'px)'

    // update the posiion attributes
    target.setAttribute('data-x', x)
    target.setAttribute('data-y', y)
}