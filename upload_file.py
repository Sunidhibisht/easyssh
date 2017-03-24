import web
from web import form

render = web.template.render('templates/')

urls = ('/', 'index')
app = web.application(urls, globals())

myform = form.Form(
    form.Dropdown('mydrop', [('value1', 'first server'), ('value2', 'second server'), ('value3', 'third server')]),
    form.Textbox("middle_server"),
    form.Textbox("middle_port",
        form.regexp('\d+', 'Usually port 22')),
    form.File('myfile'))

class index:
    def GET(self):
        form = myform()
        # make sure you create a copy of the form by calling it (line above)
        # Otherwise changes will appear globally
        return render.formtest(form)

    def POST(self):
        toshow=''
        form = myform()
        if not form.validates():
            return render.formtest(form)
        else:

            x = web.input(myfile={})
            filedir = '/tmp'

            if 'myfile' in x:
                filepath=x.myfile.filename.replace('\\','/')
                filename=filepath.split('/')[-1]
                file_send = '/tmp/' + filename
                try:
                    fout = open(filedir +'/'+ filename,'w')
                    fout.write(x.myfile.file.read())
                    fout.close()
                except IOError:
                    pass


if __name__=="__main__":
    web.internalerror = web.debugerror
    app.run()
