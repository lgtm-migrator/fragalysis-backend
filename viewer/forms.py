from django import forms
from django.conf import settings

CHOICES = [
    (0, 'validate'),
    (1, 'upload'),
]

class CSetForm(forms.Form):
    """A Django form used for uploading Computed sets at viewer/upload_cset

    Parameters
    ----------
    target_name: CharField
        The name of the target, as written in `viewer.models.Targets` that you want to upload a computed set for
    sdf_file: FileField
        The sdf file that you want to upload, containing information about the 3D structure of all molecules in the computed set.
    pdb_zip: FileField
        A zip file of apo pdb files referenced by the molecules in sdf_file (optional)
    submit_choice: CharField
        Whether to validate (0) or validate and upload (1) - displayed as a radio button
    upload_key: CharField
        The user-specific upload key generated by `viewer.views.cset_key`
    """
    target_name = forms.CharField(label='Target', max_length=100)
    sdf_file = forms.FileField(label='All compounds sdf (.sdf)')
    pdb_zip = forms.FileField(required=False, label='PDB files (.zip)')
    submit_choice = forms.CharField(widget=forms.RadioSelect(choices=CHOICES))
    upload_key = forms.CharField(label='Upload Key')


class CSetUpdateForm(forms.Form):
    """A Django form used for updating Computed sets at viewer/update_cset

    Parameters
    ----------
    target_name: CharField
        The name of the target, as written in `viewer.models.Targets` that you want to upload a computed set for
    sdf_file: FileField
        The sdf file that you want to upload, containing information about the 3D structure of all molecules in the computed set.
    pdb_zip: FileField
        A zip file of apo pdb files referenced by the molecules in sdf_file (optional)
    computed_set: CharField
        Computed set to update
    """
    target_name = forms.CharField(label='Target', max_length=100)
    sdf_file = forms.FileField(label='All compounds sdf (.sdf)')
    pdb_zip = forms.FileField(required=False, label='PDB files (.zip)')
    # computed_set = forms.CharField(label='Update', max_length=100)


class UploadKeyForm(forms.Form):
    contact_email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control', 'autocomplete':'off'}), required=True)


class TSetForm(forms.Form):
    """A Django form used for uploading Target sets at viewer/upload_tset

    Parameters
    ----------
    target_name: CharField
        The name of the target, as written in `viewer.models.Targets` that you want to upload Target set for
    target_zip: FileField
        A zip file containing a target dataset in a specific format (folders / data)
    submit_choice: CharField
        Whether to validate (0) or validate and upload (1) - displayed as a radio button
    proposal_ref: CharField
        Proposal the target should be attached to/validated with.
    contact_email: EmailField
        An email address to receive upload notifications.
    """
    target_name = forms.CharField(label='Target', max_length=100)
    target_zip = forms.FileField(required=True, label='Target data (.zip)')
    submit_choice = forms.CharField(widget=forms.RadioSelect(choices=CHOICES))

    # For Diamond, a proposal is always required. For other implementations, it may be optional or omitted.
    if settings.PROPOSAL_SUPPORTED and settings.PROPOSAL_REQUIRED:
        proposal_ref = forms.CharField(required=True, label='Proposal', max_length=200, initial='OPEN')
    elif settings.PROPOSAL_SUPPORTED:
        proposal_ref = forms.CharField(required=False, label='Proposal', max_length=200, initial='OPEN')
    else:
        proposal_ref = ''
    contact_email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control', 'autocomplete':'off'}), required=False)
