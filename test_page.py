function tableclick(e) {
    if(!e)
     e = window.event;

    if(e.target.value == "Delete")
       deleteRow( e.target.parentNode.parentNode.rowIndex );
}