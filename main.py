from app import validate_email, get_data_by_collection

def main():
    email = input('Enter your email: ')
    val = validate_email(email)

    if val['status'] is False:
        print('NaN !!! Validate email is fail')
        return

    print('Validate email is OK, please wait a second ...')
    result = {}
    cols = [
        'candidates',
        'general-informations',
        'educations',
        'experiences',
        'projects',
        'certificates',
        'award'
    ]
    for col in cols:
        query = { '_id': val['_id'] } if col == 'candidates' else {'candidateId': val['_id']}
        res = get_data_by_collection(col, query)
        result[col] = res

    print(result)
main()
'''
import uvicorn
if __name__ == '__main__':
    uvicorn.run('app.server:run', host='0.0.0.0', port=3002, reload=True)
    '''
