var lock=false
    function store(){
        var temp=document.getElementById('store')
        if(temp.getAttribute("class")=="glyphicon glyphicon-star-empty star")
        {
            temp.setAttribute("class", "glyphicon glyphicon-star star")
            temp.setAttribute("title", "取消收藏")
        }
        else{
            temp.setAttribute("class", "glyphicon glyphicon-star-empty star")
            temp.setAttribute("title", "收藏商品")
        }

    }
