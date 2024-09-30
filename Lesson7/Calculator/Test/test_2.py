from Lesson7.Calculator.Pages.Calcmainpage import CalcMain 



def test_calculator_assert(chrome_browser):
    cl = CalcMain(chrome_browser)
    cl.insert_time()
    cl.clicking_buttons()
    
    
    assert "15" in cl.wait_buttons_gettext()






    