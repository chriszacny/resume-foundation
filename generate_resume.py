from jinja2 import Environment, PackageLoader
import os
import json


class Keys:
    Phone = 'phone'
    EmailAddress = 'email_address'
    Website = 'website'
    Location = 'location'


def main():
    print('Welcome to the Zacny resume generator.')

    my_working_directory = os.path.dirname(os.path.realpath(__file__))
    defaults_file_path = os.path.join(my_working_directory, 'defaults.json')

    if os.path.exists(defaults_file_path):
        with open(defaults_file_path, 'r') as defaults_file_hdl:
            resume_variable_data = json.loads(defaults_file_hdl.read())
    else:
        resume_variable_data = {Keys.Phone: '', Keys.EmailAddress: '', Keys.Website: '',
                                Keys.Location: ''}

    email_address = input('Please enter your email address [{}]: '.format(resume_variable_data[Keys.EmailAddress]))
    phone = input('Please enter your phone [{}]: '.format(resume_variable_data[Keys.Phone]))
    website = input('Please enter your website [{}]: '.format(resume_variable_data[Keys.Website]))
    location = input('Please enter your location [{}]: '.format(resume_variable_data[Keys.Location]))

    if email_address != '':
        resume_variable_data[Keys.EmailAddress] = email_address
    if phone != '':
        resume_variable_data[Keys.Phone] = phone
    if website != '':
        resume_variable_data[Keys.Website] = website
    if location != '':
        resume_variable_data[Keys.Location] = location

    env = Environment(loader=PackageLoader('generate_resume', 'site'))
    template = env.get_template('template.html')

    with open(os.path.join(my_working_directory, 'site', 'resume.html'), 'w') as to_write:
        to_write.write(template.render(model=resume_variable_data))

    with open(defaults_file_path, 'w') as defaults_writer:
        defaults_writer.write(json.dumps(resume_variable_data))

    #TODO: Convert output to pdf, only first page.

    print('Done.')

if __name__ == '__main__':
    main()
