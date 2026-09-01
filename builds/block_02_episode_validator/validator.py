fps_defaults = (10,30,50)
record_struct =("id","frames","fps","task")

class UnidentifiedEpisode(Exception):
    pass

def faults(record):
    # This part is for finding the missing fields 
    faults_to_be_returned = []
    missing_fields = [fields for fields in record_struct if fields not in record.keys() ]
    faults_to_be_returned = faults_to_be_returned + missing_fields
    
    # This part is for finding the faulty fields     
    for field in record.keys():
        if field == "id":
            try:
                if type(record[field])!=int or record[field]<0:
                    faults_to_be_returned.append(field)
            except TypeError:
                faults_to_be_returned.append(field)
        
        elif field == "frames":
            try :
                if type(record[field])!=int or record[field]<1:
                    faults_to_be_returned.append(field)
            except TypeError:
                faults_to_be_returned.append(field)
        
        elif field == "fps":
            if type(record[field])!=int or record[field] not in fps_defaults: # I believe no need of checking exception for this 
                faults_to_be_returned.append(field)
        
        elif field =="task":
            try :
                if type(record[field])!=str or record[field]=="":
                    faults_to_be_returned.append(field)
            except TypeError:
                faults_to_be_returned.append(field)
    
    # After this part we have all the faulty and missing fields but their order might have got disturbed
    
    faults_to_be_returned.sort(key=record_struct.index)
    
    # After this part all the missing and faulty fields are there but the word missing: is not present so
    
    for index,fault_identified in enumerate(faults_to_be_returned):
        if fault_identified in missing_fields:
            faults_to_be_returned[index] = f"missing:{fault_identified}"
    
    return faults_to_be_returned

def validate_all(records):
    output = {"clean":[],"faulty":{}}
    
    for index,particular_record in enumerate(records):
        obtained_faults = faults(particular_record)
        if obtained_faults == []:
            output["clean"].append(particular_record["id"])
                 
        elif "id" in obtained_faults or "missing:id" in obtained_faults:
            raise UnidentifiedEpisode(f"record at position {index} has no usable id")
        
        else:
            output["faulty"][particular_record["id"]]=obtained_faults

    return output

def validate_logged(records, log):
    try:
        output = validate_all(records)
        
    except UnidentifiedEpisode:
        log.append("UNIDENTIFIED")
        raise
    
    return output,log


    
    
        