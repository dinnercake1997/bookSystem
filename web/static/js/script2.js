var score=0
function c1(){
    score=1
    lock=false
    s1()
    lock=true
}
function c2(){
    score=2
    lock=false
    s2()
    lock=true
}
function c3(){
    score=3
    lock=false
    s3()
    lock=true
}
function c4(){
    score=4
    lock=false
    s4()
    lock=true
}
function c5(){
    score=5
    lock=false
    s5()
    lock=true
}
    function s1(){
        lock=false
        r2()
        var temp=document.getElementById('star1')
        temp.setAttribute("class", "glyphicon glyphicon-star star");
    }
    function s2(){
        lock=false
        s1()
        r3()
        var temp=document.getElementById('star2')
        temp.setAttribute("class", "glyphicon glyphicon-star star");
    }
    function s3(){
        lock=false
        s2()
        r4()
        var temp=document.getElementById('star3')
        temp.setAttribute("class", "glyphicon glyphicon-star star");
    }
    function s4(){
        lock=false
        s3()
        r5()
        var temp=document.getElementById('star4')
        temp.setAttribute("class", "glyphicon glyphicon-star star");
    }
    function s5(){
        lock=false
        s4()
        var temp=document.getElementById('star5')
        temp.setAttribute("class", "glyphicon glyphicon-star star");
    }
    function r5(){
        var temp=document.getElementById('star5')
        temp.setAttribute("class", "glyphicon glyphicon-star-empty star");
    }
    function r4(){
        r5()
        var temp=document.getElementById('star4')
        temp.setAttribute("class", "glyphicon glyphicon-star-empty star");
    }
    function r3(){
        r4()
        var temp=document.getElementById('star3')
        temp.setAttribute("class", "glyphicon glyphicon-star-empty star");
    }
    function r2(){
        r3()
        var temp=document.getElementById('star2')
        temp.setAttribute("class", "glyphicon glyphicon-star-empty star");
    }
    function r1(){
        if(lock==true){return}
        r2()
        var temp=document.getElementById('star1')
        temp.setAttribute("class", "glyphicon glyphicon-star-empty star");
    }
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
    function eva(){        
        var temp=document.getElementById('star1')
        if(temp.getAttribute("class")=="glyphicon glyphicon-star-empty star")
        {
            alert("请打星")
            return"#"
        }
        var text=document.getElementsByTagName('textarea')[0]
        if(text.value.length==0)
        {
            alert("评价内容不能为空")
            return"#"
        }
        alert("评价成功")
        return "/web/buyer_center/?b=-1"
    }
